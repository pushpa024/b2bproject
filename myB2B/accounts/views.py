from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext, gettext_lazy as _
from django.conf import settings
from .forms import RegistrationForm
from .forms import LoginForm, form_validation_error, BusinessProfileForm, FullSaleProfileForm, PartialStakeProfileForm, SellOrLeaseProfileForm
from .models import User, Profile, FSImages, PSSImages, FSDoc, FSBusiProof, PSSDoc, PSSBusiProof, FullSale, PartialStakeSale
from .models import SLImages,SLDoc,SLBusiProof,SellOrLeaseAssets
from .models import StripeCustomer

from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.http import HttpResponse


from .token import account_activation_token
import uuid
from .helpers import send_forget_password_email
import stripe

class LoginView(View):
    template_name = "accounts/login-new.html"
    form_class = LoginForm
    login_error = _("Invalid email or password.")
    login_success = _("Successfully logged in.")

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to='/')
        next_url = request.GET.get("next", "/")
        context = {
            "form": self.form_class(),
            "next_url": next_url,
            "title": "Login | Huntment"
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        post_data = request.POST.copy()
        next_url = post_data.get('next', '/')
        email = post_data.get('email', None)
        password = post_data.get('password', None)

        if email and password:
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, self.login_success)
                return redirect(to=next_url)
            else:
                messages.add_message(request, messages.ERROR, self.login_error)
                context = {
                    "form": self.form_class(request.POST.copy()),
                    "error": True,
                    "next_url": next_url
                }
                return render(request, self.template_name, context)
        else:
            messages.add_message(request, messages.ERROR, self.login_error)
            context = {
                "form": self.form_class(request.POST.copy()),
                "error": True,
                "next_url": next_url
            }
            return render(request, self.template_name, context)


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        r_url = '/'
        try:
            r_url = settings.LOGOUT_REDIRECT_URL
            messages.success(request,"Logged out succussfully!")
        except AttributeError as e:
            r_url = '/'
        finally:
            return redirect(to=r_url)


class UserRegistration(View):
    template_name = "accounts/register-new.html"
    form_class = RegistrationForm

    def get(self, request, *args, **kwargs):
        context = {
            "title": "Sign up | Huntment",
            "form": self.form_class(),
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        register_form = self.form_class(request.POST.copy())
        if register_form.is_valid():
            # user = register_form.save(commit = "False")

            first_name = register_form.cleaned_data.get("first_name", "")
            last_name = register_form.cleaned_data.get("last_name", "")
            email = register_form.cleaned_data.get("email", "")
            password = register_form.cleaned_data.get("password", "")
            user = User.objects.create(email=email)
            user.username = email
            user.first_name = first_name
            user.last_name = last_name
            user.set_password(password)
            user.is_active = False
            user.is_staff = False
            user.is_superuser = False
            user.save()

            val = activateEmail(request,user,register_form.cleaned_data.get('email'))
            # success_msg = """
            # <b>Your account has been successfully created!</b> 
            # <div><small>An activation email has been sent to {email}. Plase click
            # on the link to activate your account. To login please <a href='/accounts/login/'>click here</a>.
            # </small></div>
            # """.format(email=user.email)
            # success_msg = "Your account has been successfully created!"
            # messages.add_message(request, messages.SUCCESS, success_msg)
            if val:
                context = {
                    "email" : email,
                    "name" : first_name
                }
        
                return render(request,"accounts/email/emailconfirm.html", context)
            else:
                return render(request,"accounts/email/emailerror.html")
        
                # return redirect(to=reverse('register-new'))
           
        else:
            err_msg = "Account creation failed!. Please correct the following errors."
            messages.add_message(request, messages.ERROR, err_msg)
            context = {
                "message": err_msg,
                "form": self.form_class(request.POST.copy()),
            }
            return render(request, self.template_name, context)


def activateEmail(request,user,to_email):
    # messages.success(request,f'Dear <b>{user}</b>, please check mail {to_email} and activate your account')
    mail_subject = 'Activate your huntment user account.'
    message = render_to_string('accounts/email/emailsend.html', {
        'user': user.first_name,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    email.content_subtype = 'html' 
    if email.send():
        context = {
            "email" : to_email,
            "name" : user.first_name
        }
        
        # messages.success(request, f'Dear {user.first_name}, please go to you email {to_email} inbox and click on \
        #     received activation link to confirm and complete the registration. Note: Check your spam folder.')
        return True
    else:
        # messages.error(request, f'Problem sending confirmation email to {to_email}, check if you typed it correctly.')
        return False

def activate(request, uidb64, token):
        User = get_user_model()
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
            messages.error(request, 'Activation failed! Please contact support!')

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()

            # messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
            # return redirect('login-new')
            return render(request,"accounts/email/emailcongrats.html")
        else:
            if user is None:
                messages.error(request, 'Activation link is invalid! Please register again!')
            else:
                messages.error(request, 'Activation link is invalid! Please register again!')
                user.delete()

        return redirect('home')



class BusinessProfile(View):
    template_name = "accounts/form/businessform.html"
    # form_class = RegistrationForm

    def get(self, request, *args, **kwargs):
        context = {
            "title": "Business Profile | Huntment",
            # "form": self.form_class(),
        }
        return render(request, self.template_name, context)


class FranchiseProfile(View):
    template_name = "accounts/form/franchise_form.html"
    # form_class = RegistrationForm

    def get(self, request, *args, **kwargs):
        context = {
            "title": "Franchise Profile | Huntment",
            # "form": self.form_class(),
        }
        return render(request, self.template_name, context)   


class InvestorBuyerProfile(View):
    template_name = "accounts/form/investor_buyer.html"
    # form_class = RegistrationForm

    def get(self, request, *args, **kwargs):
        context = {
            "title": "Investor & Buyer Profile | Huntment",
            # "form": self.form_class(),
        }
        return render(request, self.template_name, context)  

def load_more(request):
    userid = request.user.id
    
    fs_obj = list(FullSale.objects.filter(user_id=userid).values())
   
    fsdata = []
    for i in fs_obj:
       
        fsitem = {
           'companyName': i["companyName"],
           'inputEmail': i["inputEmail"],
           'url': reverse("business_sale_cust", kwargs={"id": i["id"], "btype":i["interested"]})
        }
        fsdata.append(fsitem)
    pss_obj = list(PartialStakeSale.objects.filter(user_id=userid).values())
    pssdata = []
    for j in pss_obj:
       
        pssitem = {
           'companyName': j["companyName"],
           'inputEmail': j["inputEmail"],
           'url': reverse("business_sale_cust", kwargs={"id": j["id"], "btype":j["interested"]})
        }
        pssdata.append(pssitem)

    sl_obj =list(SellOrLeaseAssets.objects.filter(user_id=userid).values())
    sldata = []
    for k in sl_obj:
        slitem = {
            'companyName': k["companyName"],
            'inputEmail' : k["inputEmail"],
            'url' : reverse("business_sale_cust",kwargs={"id": k["id"], "btype": k["interested"]})
        }
        sldata.append(slitem)

   
    data = {
        'fs': fsdata,
        'pss': pssdata,
        'sl': sldata
    }
    return JsonResponse(data=data)
    

class HeaderProfile(View):
    template_name = "base/base.html"

    
    def get(self, request, *args, **kwargs):

        userid = request.user.id
        print(userid)

        context = {
            "title": "Investor & Buyer Profile | Huntment",
        }
        return render(request, self.template_name, context) 

@login_required(login_url='login-new')
def addBusinessProfile(request):
    if request.method == "POST":
        form_FS = BusinessProfileForm(request.POST or None, request.FILES or None)
        form_PS = PartialStakeProfileForm(request.POST or None, request.FILES or None)
        form_SL = SellOrLeaseProfileForm(request.POST or None, request.FILES or None)
        images = request.FILES.getlist("facility_photos")
        d_files = request.FILES.getlist("brochure_doc")
        b_files = request.FILES.getlist("business_proof")
        
        interested = request.POST.get('interested')
        print("aaaaaaaaaaaaaaaaaaa")
        print(interested)
        try:
            if form_FS.is_valid() and  interested == "fullSale":
                bProfile = form_FS.save(commit=False)
                bProfile.user = request.user
                # bProfile.uuid = uuid.uuid4
                bProfile.save()
                image_list = []
                d_list = []
                b_list =[]
                for i in images:
                    new_file = FSImages(facility_photos = i)
                    FSImages.objects.create(business_profile=bProfile, facility_photos=i)
                    image_list.append(new_file.facility_photos.url)
                
                for j in d_files:
                    new_file_d = FSDoc(brochure_doc = j)
                    FSDoc.objects.create(business_profile=bProfile, brochure_doc=j)

                for k in b_files:
                    new_file_b = FSBusiProof(business_proof = k)
                    FSBusiProof.objects.create(business_profile=bProfile, business_proof=k) 

                messages.success(request,"Business full sale profile created successfully")
                # return redirect("successpage")
                context = {"form" : bProfile, "images" : image_list}
                return render(request,"accounts/businessForSale/businessforsalecustomer.html", context)        

            elif form_PS.is_valid() and interested == "partialBusiness":
                bProfile = form_PS.save(commit=False)
                bProfile.user = request.user
                bProfile.save()
                # file_list = []
                image_list = []
                d_list = []
                b_list =[]
                # for i in files:
                #     new_file = PSSImages(facility_photos = i)
                #     PSSImages.objects.create(business_profile=bProfile, facility_photos=i)
                #     file_list.append(new_file.facility_photos.url)
                # images = PSSImages.objects.all()
                for i in images:
                    new_file = PSSImages(facility_photos = i)
                    PSSImages.objects.create(business_profile=bProfile, facility_photos=i)
                    image_list.append(new_file.facility_photos.url)
                
                for j in d_files:
                    new_file_d = PSSDoc(brochure_doc = j)
                    PSSDoc.objects.create(business_profile=bProfile, brochure_doc=j)

                for k in b_files:
                    new_file_b = PSSBusiProof(business_proof = k)
                    PSSBusiProof.objects.create(business_profile=bProfile, business_proof=k) 

                messages.success(request,"Business partial sale profile created successfully")
                context = {"form" : bProfile, "images" : image_list}
                return render(request,"accounts/businessForSale/businessforsalecustomer.html", context) 
                # return redirect("successpage")

            elif form_SL.is_valid() and  interested == "sellingLeasing":
                bProfile = form_SL.save(commit=False)
                bProfile.user = request.user
                bProfile.save()
                image_list = []
                d_list = []
                b_list =[]
                print("ddddd")
                for i in images:
                    print("iniiiiiiii")
                    new_file = SLImages(facility_photos = i)
                    SLImages.objects.create(business_profile=bProfile, facility_photos=i)
                    image_list.append(new_file.facility_photos.url)
                
                for j in d_files:
                    new_file_d = SLDoc(brochure_doc = j)
                    SLDoc.objects.create(business_profile=bProfile, brochure_doc=j)

                for k in b_files:
                    new_file_b = SLBusiProof(business_proof = k)
                    SLBusiProof.objects.create(business_profile=bProfile, business_proof=k) 

                messages.success(request,"Sell or Lease business profile created successfully")
                # return redirect("successpage")
                context = {"form" : bProfile, "images" : image_list}
                return render(request,"accounts/businessForSale/businessforsalecustomer.html", context)    
            
            else:
                messages.success(request,"error in the form, please fill all the details")
        except:
            messages.error(request, f'Problem with business profile creation')

        # return render(request,"accounts/form/businessform.html",{"form":form_FS})       

    return render(request,"accounts/form/businessform2.html")

def successpage(request):
    return render(request,"accounts/businessForSale/Business for sale-customer.html")        

# @login_required(login_url='login-new')
# class BusinessSaleCustomerLoggedIn(View):

#     def post(self, request, id, btype ):
#         print("inside1")
#         if btype == "fullSale":
#             print("inside2")
#             bsdetails = get_object_or_404(FullSale, id=id)
#             context = {'bsdetails': bsdetails}
#         else:
#             bsdetails = get_object_or_404(PartialStakeSale, id=id)
#             context = {'bsdetails': bsdetails}
#         return render(request,"accounts/businessForSale/businessforsale-loggind.html", context)     

@login_required(login_url='login-new')
def BusinessSaleCustomerLoggedIn(request, id, btype ):
    print("inside1")
    print(id)
    if btype == "fullSale":
        print("inside2")
        bsdetails = get_object_or_404(FullSale, id=id)
        context = {'bsdetails': bsdetails}

    elif btype == "sellingLeasing":
         print("inside22")
         bsdetails = get_object_or_404(SellOrLeaseAssets, id=id)
         context = {'bsdetails': bsdetails}

    elif btype == "partialBusiness":
        bsdetails = get_object_or_404(PartialStakeSale, id=id)
        context = {'bsdetails': bsdetails}

    else:
         messages.error(request, 'Problem with business detials, contact support.')
         return render(request,"base/header-menu/business_sale1.html")

    return render(request,"accounts/businessForSale/businessforsale-loggind.html", context)     


def email_error(request):
    return render(request, 'scoringsheet.html', {})

def ChangePassword(request,token):
    context={}
    try:
        user_obj = User.objects.filter(forget_password_token=token).first()
        if user_obj is None:
            messages.error(request,"Token is invalid or already used to change password!")
            return redirect('forgetpassword')

        context = {
            'user_id' : user_obj.id
        }


        print(user_obj)
        #if any post data submitted from changepassword.html
        if request.method == "POST":
            new_password = request.POST.get("password")
            confirm_password = request.POST.get("password_confirm")
            user_id = request.POST.get("user_id")

            if user_id is None:
                messages.success(request, "Username doesn't exists")
                return redirect('forgetpassword')

            if new_password != confirm_password:
                messages.error(request, "Entered passwords does not match!")
                return redirect('')

            user_obj.set_password(new_password)
            user_obj.save()
            user_obj.forget_password_token = None
            user_obj.save()
            messages.success(request,"Password changed successfully!")

            return redirect('login-new')

        
    except Exception as e:
        print(e)    
    return render(request, "accounts/changepassword.html", context)

def ForgetPassword(request):
    try:
        if request.method == "POST":
            email = request.POST.get("mail")
            
        if not User.objects.filter(email=email).first():
            messages.info(request, "Entered Email is not registered with our system! Please re-enter the correct email.")
            return redirect('forgetpassword')
        
        user_obj = User.objects.get(email=email)
        token = str(uuid.uuid4())
        user_obj.forget_password_token = token
        user_obj.save()
        username = user_obj.first_name
        send_forget_password_email(request,email,token,username)
        messages.success(request, "An email with link to change the password is sent to your email address.")
       
        return redirect('forgetpassword')

    except Exception as e:
        print(e)
    return render(request, "accounts/forgetpassword.html")

@login_required
def stripepay(request):
    return render(request, 'accounts/stripepay/stripepage.html')


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=request.user.id if request.user.is_authenticated else None,
                # success_url=domain_url + 'accounts/success_payment?session_id={CHECKOUT_SESSION_ID}',
                # cancel_url=domain_url + 'accounts/cancel_payment/',
                success_url=request.build_absolute_uri(reverse('successStripe'))+'?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'accounts/cancel_payment/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'price': settings.STRIPE_PRICE_ID,
                        'quantity': 1,
                    }
                ],
                 
            )
            print(checkout_session['id'])
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})

@login_required
def successStripe(request):
    return render(request, 'accounts/stripepay/successStripe.html')


@login_required
def cancelStripe(request):
    return render(request, 'accounts/stripepay/cancelStripe.html')


@csrf_exempt
def stripe_webhook_view(request):
  # payload = request.body

  # # For now, you only need to print out the webhook payload so you can see
  # # the structure.
  # print(payload)
  payload = request.body
  sig_header = request.META['HTTP_STRIPE_SIGNATURE']
  event = None

  try:
    event = stripe.Webhook.construct_event(
      payload, sig_header, settings.STRIPE_ENDPOINT_SECRET
    )
  except ValueError as e:
    # Invalid payload
    return HttpResponse(status=400)
  except stripe.error.SignatureVerificationError as e:
    # Invalid signature
    return HttpResponse(status=400)

     # Handle the checkout.session.completed event
  if event['type'] == 'checkout.session.completed':
    session = event['data']['object']

    # Fulfill the purchase...
    # fulfill_order(session)
    client_reference_id = session.get('client_reference_id')
    stripe_customer_id = session.get('id')
    stripe_subscription_id = session.get('payment_intent')

    # Get the user and create a new StripeCustomer
    user = User.objects.get(id=client_reference_id)
    StripeCustomer.objects.create(
        user=user,
        stripeCustomerId=stripe_customer_id,
        stripeSubscriptionId=stripe_subscription_id,
    )
    print(user.username + ' just subscribed.')
  
  # Passed signature verification
  return HttpResponse(status=200)
  
