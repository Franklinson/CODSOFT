from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm, PhoneNumberForm, EmailForm, AddressForm, SocialMediaForm, InteractionLogForm, PhoneNumberFormSet, EmailFormSet, AddressFormSet, SocialMediaFormSet, InteractionLogFormSet
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
    cont = Contact.objects.all()
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('todo_list')
    return render(request, 'contacts/delete.html', {'con': contact, 'cont': cont})


def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact_form = ContactForm(request.POST, request.FILES, instance=contact)
        phone_formset = PhoneNumberFormSet(request.POST, request.FILES, instance=contact, prefix='phone')
        email_formset = EmailFormSet(request.POST, request.FILES, instance=contact, prefix='email')
        address_formset = AddressFormSet(request.POST, request.FILES, instance=contact, prefix='address')
        social_media_formset = SocialMediaFormSet(request.POST, request.FILES, instance=contact, prefix='social_media')
        interaction_log_formset = InteractionLogFormSet(request.POST, request.FILES, instance=contact, prefix='interaction_log')

        if contact_form.is_valid() and phone_formset.is_valid() and email_formset.is_valid() and address_formset.is_valid() and social_media_formset.is_valid() and interaction_log_formset.is_valid():
            contact = contact_form.save()
            phone_formset.instance = contact
            phone_formset.save()
            email_formset.instance = contact
            email_formset.save()
            address_formset.instance = contact
            address_formset.save()
            social_media_formset.instance = contact
            social_media_formset.save()
            interaction_log_formset.instance = contact
            interaction_log_formset.save()
            return redirect('contact_detail', pk=contact.pk)  # Replace with your success URL
    else:
        contact_form = ContactForm(instance=contact)
        phone_formset = PhoneNumberFormSet(instance=contact, prefix='phone')
        email_formset = EmailFormSet(instance=contact, prefix='email')
        address_formset = AddressFormSet(instance=contact, prefix='address')
        social_media_formset = SocialMediaFormSet(instance=contact, prefix='social_media')
        interaction_log_formset = InteractionLogFormSet(instance=contact, prefix='interaction_log')

    context = {
        'contact_form': contact_form,
        'phone_formset': phone_formset,
        'email_formset': email_formset,
        'address_formset': address_formset,
        'social_media_formset': social_media_formset,
        'interaction_log_formset': interaction_log_formset,
    }
    return render(request, 'contacts/edit_contact.html', context)