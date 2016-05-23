from django.contrib import admin
from claims.models import Claim, Offer, Questionnaire


admin.site.register(Claim)
admin.site.register(Offer)
admin.site.register(Questionnaire)
