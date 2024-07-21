from django import forms
from .models import Contact, PhoneNumber, Email, Address, SocialMedia, InteractionLog
from django.forms import inlineformset_factory

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


PhoneNumberFormSet = inlineformset_factory(Contact, PhoneNumber, form=PhoneNumberForm, extra=1, can_delete=True)
EmailFormSet = inlineformset_factory(Contact, Email, form=EmailForm, extra=1, can_delete=True)
AddressFormSet = inlineformset_factory(Contact, Address, form=AddressForm, extra=1, can_delete=True)
SocialMediaFormSet = inlineformset_factory(Contact, SocialMedia, form=SocialMediaForm, extra=1, can_delete=True)
InteractionLogFormSet = inlineformset_factory(Contact, InteractionLog, form=InteractionLogForm, extra=1, can_delete=True)
