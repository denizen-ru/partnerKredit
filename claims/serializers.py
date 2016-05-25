from rest_framework import serializers
from claims.models import Claim, Questionnaire, Offer
from accounts.models import Partner, CreditOrganization


class ClaimSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Claim
        fields = ('id', 'creation_date', 'sending_date',
                  'questionnaire', 'offer', 'status')


class QuestionnaireSerializer(serializers.HyperlinkedModelSerializer):
    partner = serializers.PrimaryKeyRelatedField(queryset=Partner.objects.all())

    class Meta:
        model = Questionnaire
        fields = ('id', 'creation_date', 'changing_date', 'client_name',
                  'birthday', 'phone_number', 'passport', 'scoring_points',
                  'partner',)


class OfferSerializer(serializers.HyperlinkedModelSerializer):
    credit_organization = serializers.PrimaryKeyRelatedField(
        queryset=CreditOrganization.objects.all())

    class Meta:
        model = Offer
        fields = ('id', 'creation_date', 'changing_date',
                  'rotation_beginning_date', 'rotation_ending_date', 'title',
                  'offer_type', 'min_scoring_points', 'max_scoring_points',
                  'credit_organization',)
