from django.contrib import admin
from accounts.models import SuperUser, Partner, CreditOrganization

admin.site.register(SuperUser)
admin.site.register(Partner)
admin.site.register(CreditOrganization)
