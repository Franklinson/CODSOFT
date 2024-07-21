from django import forms
from .models import Contact, PhoneNumber, Email, Address, SocialMedia, InteractionLog

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'birthday', 'anniversary', 'company', 'job_title', 'department', 'notes', 'tags', 'profile_picture']

class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = PhoneNumber
        fields = ['phone_type', 'number']

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['email_type', 'email']

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['address_type', 'address']

class SocialMediaForm(forms.ModelForm):
    class Meta:
        model = SocialMedia
        fields = ['platform', 'url']

class InteractionLogForm(forms.ModelForm):
    class Meta:
        model = InteractionLog
        fields = ['log']
