from django import forms

class PasswordForm(forms.Form):
    length = forms.IntegerField(label='Password Length', min_value=1)
    purpose = forms.CharField(label='Purpose', max_length=100)