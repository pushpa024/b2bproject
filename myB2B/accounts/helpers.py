from django.core.mail import send_mail,EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site


def send_forget_password_email(request,toemail,token, username):
	

    mail_subject = 'Change Password for huntment user account.'
    message = render_to_string('accounts/email/emailresend.html', {
        'domain': get_current_site(request).domain,
        'token': token,
        'username': username,
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[toemail])
    email.content_subtype = 'html' 
    if email.send():
        print("mail sent")
                
        # messages.success(request, f'Dear {user.first_name}, please go to you email {to_email} inbox and click on \
        #     received activation link to confirm and complete the registration. Note: Check your spam folder.')
        return True
    else:
        # messages.error(request, f'Problem sending confirmation email to {to_email}, check if you typed it correctly.')
        return False