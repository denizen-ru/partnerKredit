from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    def __str__(self):
        return self.username

    def __unicode__(self):
        return self.username


class SuperUser(CustomUser):

    class Meta:
        verbose_name = "Super User"
        verbose_name_plural = "Super Users"


class Partner(CustomUser):

    class Meta:
        verbose_name = "Partner"
        verbose_name_plural = "Partners"


class CreditOrganization(CustomUser):

    class Meta:
        verbose_name = "Credit Organization"
        verbose_name_plural = "Credit Organizations"
