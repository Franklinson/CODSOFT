from django.contrib import admin

from django.contrib import admin
from .models import Contact, PhoneNumber, Email, Address, SocialMedia, InteractionLog

class PhoneNumberInline(admin.TabularInline):
    model = PhoneNumber
    extra = 1

class EmailInline(admin.TabularInline):
    model = Email
    extra = 1

class AddressInline(admin.TabularInline):
    model = Address
    extra = 1

class SocialMediaInline(admin.TabularInline):
    model = SocialMedia
    extra = 1

class InteractionLogInline(admin.TabularInline):
    model = InteractionLog
    extra = 1

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = [PhoneNumberInline, EmailInline, AddressInline, SocialMediaInline, InteractionLogInline]

admin.site.register(PhoneNumber)
admin.site.register(Email)
admin.site.register(Address)
admin.site.register(SocialMedia)
admin.site.register(InteractionLog)

