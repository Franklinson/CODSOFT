from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm, PhoneNumberForm, EmailForm, AddressForm, SocialMediaForm, InteractionLogForm
from .models import Contact

def create_contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST, request.FILES)
        phone_form = PhoneNumberForm(request.POST)
        email_form = EmailForm(request.POST)
        address_form = AddressForm(request.POST)
        social_media_form = SocialMediaForm(request.POST)
        interaction_log_form = InteractionLogForm(request.POST)

        if all([contact_form.is_valid(), phone_form.is_valid(), email_form.is_valid(), address_form.is_valid(), social_media_form.is_valid(), interaction_log_form.is_valid()]):
            contact = contact_form.save()
            phone = phone_form.save(commit=False)
            phone.contact = contact
            phone.save()
            email = email_form.save(commit=False)
            email.contact = contact
            email.save()
            address = address_form.save(commit=False)
            address.contact = contact
            address.save()
            social_media = social_media_form.save(commit=False)
            social_media.contact = contact
            social_media.save()
            interaction_log = interaction_log_form.save(commit=False)
            interaction_log.contact = contact
            interaction_log.save()
            return redirect('home')
    else:
        contact_form = ContactForm()
        phone_form = PhoneNumberForm()
        email_form = EmailForm()
        address_form = AddressForm()
        social_media_form = SocialMediaForm()
        interaction_log_form = InteractionLogForm()

    context = {
        'contact_form': contact_form,
        'phone_form': phone_form,
        'email_form': email_form,
        'address_form': address_form,
        'social_media_form': social_media_form,
        'interaction_log_form': interaction_log_form,
    }
    return render(request, 'contacts/create_contact.html', context)


def deleteContact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('todo_list')
    return render(request, 'contacts/delete.html', {'rem': contact})