from django import forms
from .models import User, BusinessProfile, FullSale, PartialStakeSale, SellOrLeaseAssets



class LoginForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"class": "form-control py-2", "placeholder":"Your Email"}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class":"form-control py-2", "placeholder":"Your Password"}))


class RegistrationForm(forms.Form):
    # first_name = forms.CharField(required=True,)
    # last_name = forms.CharField(required=False,)
    # email = forms.EmailField(required=True,)
    # password = forms.CharField(required=True,)
    # password_confirm = forms.CharField(required=True,)

    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"form-control py-2 bg-transparent text-white border-0 border-bottom rounded-0 border_huntment", "autocomplete": "off", "placeholder":"Your First Name"}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={"class":"form-control py-2 bg-transparent text-white border-0 border-bottom rounded-0 border_huntment", "autocomplete": "off", "placeholder":"Your Last Name"}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"class": "form-control py-2 bg-transparent text-white border-0 border-bottom rounded-0 border_huntment", "autocomplete": "off", "placeholder":"Your Email"}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class":"form-control py-2 text-white bg-transparent border-0 border-bottom rounded-0 border_huntment", "placeholder":"Your Password"}))
    password_confirm = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class":"form-control py-2 text-white bg-transparent border-0 border-bottom rounded-0 border_huntment", "placeholder":"Your Password again"}))

    def clean(self):
        email = self.cleaned_data.get('email', None)
        password = self.cleaned_data.get('password', None)
        password_confirm = self.cleaned_data.get('password_confirm', None)
        if password and password_confirm:
            if password != password_confirm:
                msg = forms.ValidationError("Passwords do not match!")
                self.add_error("password", msg)
                self.add_error("password_confirm", msg)
        if email:
            user = User.objects.filter(email=email.strip())
            if user.exists():
                msg = forms.ValidationError("User with this email already exists.")
                self.add_error("email", msg)

        return self.cleaned_data

# class ProfileForm1(forms.Form):
#     first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"form-control py-2 text-white bg-transparent border-0 border-bottom rounded-0 border_huntment", "placeholder":"Your First Name"}))
#     company_name = forms.CharField(required=False, widget=forms.TextInput(attrs={"class":"form-control py-2 bg-transparent border-0 border-bottom rounded-0 border_huntment", "placeholder":"Your Last Name"}))
#     email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"class": "form-control py-2 bg-transparent border-0 border-bottom rounded-0 border_huntment", "placeholder":"Your Email"}))
#     contact_no = forms.CharField(required=False, widget=forms.TextInput(attrs={"class":"form-control py-2 bg-transparent border-0 border-bottom rounded-0 border_huntment", "placeholder":"Your Last Name"}))

# class ProfileForm(forms.ModelForm):
#     inputFname = forms.CharField(max_length=255)
#     phone = forms.CharField(max_length=255)
#     companyName = forms.CharField(max_length=255)
#     inputEmail = forms.EmailField()

#     class Meta:
#         model = Profile
#         fields = '__all__'
#         exclude = ['user']

class BusinessProfileForm(forms.ModelForm):
    class Meta:
        # model = BusinessProfile
        model = FullSale
        fields = '__all__'
        exclude = ['user']       

class FullSaleProfileForm(forms.ModelForm):
    class Meta:
        model = FullSale
        fields = '__all__'
        exclude = ['user']

class PartialStakeProfileForm(forms.ModelForm):
    class Meta:
        model = PartialStakeSale
        fields = '__all__'
        exclude = ['user']  

class SellOrLeaseProfileForm(forms.ModelForm):
    class Meta:
        model = SellOrLeaseAssets
        fields = '__all__'
        exclude = ['user']  

def form_validation_error(form):
    msg = ""
    for field in form:
        for error in field.errors:
            msg += "%s: %s \\n" % (field.label if hasattr(field, 'label') else 'Error', error)
    return msg