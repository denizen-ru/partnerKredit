from django.db import models
from accounts.models import SuperUser, Partner, CreditOrganization

OFFER_TYPE_CHOICES = (
    ('CC', 'Consumer credit'),
    ('MG', 'Mortgage'),
    ('CL', 'Car loan'),
    ('SME', 'SME credit')
)

CLAIM_STATUS_CHOICES = (('NEW', 'New claim'), ('SENT', 'Sended claim'))


class Offer(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True,
                                         verbose_name='Creation date/time')
    changing_date = models.DateTimeField(auto_now=True,
                                         verbose_name='Changing date/time')
    rotation_beginning_date = models.DateTimeField(
        verbose_name='Rotation beginning date/time')
    rotation_ending_date = models.DateTimeField(
        verbose_name='Rotation ending date/time')
    title = models.CharField(max_length=255, verbose_name="Offer's title")
    offer_type = models.CharField(max_length=3, choices=OFFER_TYPE_CHOICES)
    min_scoring_points = models.IntegerField()
    max_scoring_points = models.IntegerField()
    credit_organization = models.ForeignKey(CreditOrganization,
                                            related_name='offer')

    class Meta:
        verbose_name = "Offer"
        verbose_name_plural = "Offers"

    def __str__(self):
        return self.title


class Questionnaire(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True,
                                         verbose_name='Creation date/time')
    changing_date = models.DateTimeField(auto_now=True,
                                         verbose_name='Changing date/time')
    client_name = models.CharField(max_length=255,
                                   verbose_name="Client's full name")
    birthday = models.DateField(verbose_name="Client's birthday")
    phone_number = models.CharField(max_length=50,
                                    verbose_name="Client's phone")
    passport = models.CharField(max_length=100,
                                verbose_name="Client's passport")
    scoring_points = models.IntegerField()
    partner = models.ForeignKey(Partner, related_name='questionnaires')

    class Meta:
        verbose_name = "Questionnaire"
        verbose_name_plural = "Questionnaires"

    def __str__(self):
        return self.client_name


class Claim(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True,
                                         verbose_name='Creation date/time')
    sending_date = models.DateTimeField(verbose_name='Sending date/time')
    questionnaire = models.ForeignKey(Questionnaire, related_name='claim',
                                      on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, related_name='claim',
                              on_delete=models.CASCADE)
    status = models.CharField(max_length=4, choices=CLAIM_STATUS_CHOICES)

    class Meta:
        verbose_name = "Claim"
        verbose_name_plural = "Claims"

    def __str__(self):
        return '{} - {}'.format(self.questionnaire, self.offer)
