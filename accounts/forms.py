from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from accounts.models import CustomUser, SuperUser, Partner, CreditOrganization


class CustomUserCreationForm(UserCreationForm):

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            CustomUser._default_manager.get(username=username)
        except CustomUser.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


class SuperUserCreationForm(UserCreationForm):

    class Meta:
        model = SuperUser
        fields = ('username', 'password')


class PartnerCreationForm(UserCreationForm):

    class Meta:
        model = Partner
        fields = ('username', 'password')


class CreditOrganizationCreationForm(UserCreationForm):

    class Meta:
        model = CreditOrganization
        fields = ('username', 'password')
