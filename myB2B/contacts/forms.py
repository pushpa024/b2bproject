from django import forms


class BasicContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "form-control py-2", "placeholder": "Name", "oninput":"nameChange()"}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"class": "form-control py-2", "placeholder": "Email", "oninput":"mailChange()"}))
    country = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "form-control py-2", "placeholder": "Country", "oninput":"countryChange()"}))
    phone = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "form-control py-2", "placeholder": "Phone", "oninput":"phoneChange()"}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={"class": "form-control py-2", "placeholder": "Message", "oninput":"msgChange()"}))

    def clean(self):
        email = self.cleaned_data.get('email', None)
        message = self.cleaned_data.get('message', '').strip()
        if not email:
            msg = forms.ValidationError("please enter a valid email address.")
            self.add_error("email", msg)
        if not message:
            msg = forms.ValidationError("please add your message.")
            self.add_error("message", msg)

        return self.cleaned_data
