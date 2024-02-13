from django.shortcuts import render, redirect, reverse
from django.views import View
from django.conf import settings
from django.template.defaultfilters import linebreaks
from django.contrib import messages
from .forms import BasicContactForm
from .models import BasicContact
from notifications.api import EmailNotification


class BasicContactView(View):
    template_name = "contacts/contact_us.html"
    form_class = BasicContactForm

    def get(self, request, *args, **kwargs):
        context = {
            "form": self.form_class(),
            "title": "Contact Us | Huntment"
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        contact_form = self.form_class(request.POST.copy())
        if contact_form.is_valid():
            name = contact_form.cleaned_data.get("name", "")
            email = contact_form.cleaned_data.get("email", "")
            country = contact_form.cleaned_data.get("country", "")
            phone = contact_form.cleaned_data.get("phone", "")
            message = contact_form.cleaned_data.get("message", "")
            contact = BasicContact.objects.create(email=email)
            contact.name = name
            contact.country = country
            contact.phone = phone
            contact.message = message
            # later we will change and use a proper email template.
            email_body = """
            <p>You have a new contact message. Here are the details.</p>
            <div>
            <div><b>Name: </b> <span>{name}</span></div>
            <div><b>Email: </b> <span>{email}</span></div>
            <div><b>Phone: </b> <span>{phone}</span></div>
            <div><b>Country: </b> <span>{country}</span></div>
            <div><b>Message: </b> <p>{message}</p></div>
            </div>
            """.format(name=contact.name,
                       email=contact.email,
                       phone=contact.phone,
                       country=contact.country,
                       message=linebreaks(contact.message))
            contact.save()
            try:
                email_notification = EmailNotification()
                email_notification.subject = "Contact from {}".format(name)
                email_notification.message = email_body
                email_notification.sender = settings.CONTACTS_NOTIFICATION_SENDER
                email_notification.receivers = settings.BASIC_CONTACT_RECEIVERS
                email_notification.send()
            except Exception as e:
                print(e)


            # after this we need to send email job with details to Redis. and the notification app will take over
            success_msg = """
                    <b>Your message has been successfully sent!</b> 
                    <div><small>Thank you {name} for contacting us. Our team will soon be notified of your message
                     and will get back to you as soon as possible.</small></div>
                    """.format(name=name)
            messages.add_message(request, messages.SUCCESS, success_msg)
            return redirect(to=reverse('basic_contact'))
        else:
            err_msg ="""
                    <b>Message sending failed!</b> 
                    <div><small>We are unable to deliver your message. Please make the corrections and try again.</small></div>
                    """
            messages.add_message(request, messages.ERROR, err_msg)
            context = {
                "message": err_msg,
                "form": self.form_class(request.POST.copy()),
                "title": "Contact Us | Huntment"
            }
            return render(request, self.template_name, context)





