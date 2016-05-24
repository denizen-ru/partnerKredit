from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from accounts.models import CustomUser, SuperUser, Partner, CreditOrganization
from accounts.forms import (
    CustomUserCreationForm, SuperUserCreationForm,
    PartnerCreationForm, CreditOrganizationCreationForm)


class CustomUserAdmin(UserAdmin):
    form = CustomUserCreationForm


class SuperUserAdmin(UserAdmin):
    list_display = ('username',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')}
         ),
    )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    form = SuperUserCreationForm


class PartnerAdmin(UserAdmin):
    list_display = ('username',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')}
         ),
    )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    form = PartnerCreationForm


class CreditOrganizationAdmin(UserAdmin):
    list_display = ('username',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')}
         ),
    )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    form = CreditOrganizationCreationForm


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(SuperUser, SuperUserAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(CreditOrganization, CreditOrganizationAdmin)
