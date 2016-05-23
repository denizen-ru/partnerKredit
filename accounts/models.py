from django.contrib.auth.models import User
from django.db import models


class SuperUser(models.Model):
    user = models.OneToOneField(User, unique=True, related_name="superuser")

    class Meta:
        verbose_name = "Super User"
        verbose_name_plural = "Super Users"

    def __str__(self):
        return self.user.username


class Partner(models.Model):
    user = models.OneToOneField(User, unique=True, related_name="partner")

    class Meta:
        verbose_name = "Partner"
        verbose_name_plural = "Partners"

    def __str__(self):
        return self.user.username


class CreditOrganization(models.Model):
    user = models.OneToOneField(User, unique=True, related_name="creditorganization")

    class Meta:
        verbose_name = "Credit Organization"
        verbose_name_plural = "Credit Organizations"

    def __str__(self):
        return self.user.username
