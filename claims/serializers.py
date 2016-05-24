from rest_framework import serializers
from claims.models import Claim, Questionnaire, Offer
from accounts.models import Partner, CreditOrganization


class ClaimSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Claim
        fields = ('creation_date', 'sending_date',
                  'questionnaire', 'offer', 'status')


class QuestionnaireSerializer(serializers.HyperlinkedModelSerializer):
    partner = serializers.SlugRelatedField(queryset=Partner.objects.all(),
                                           slug_field='username')

    class Meta:
        model = Questionnaire
        fields = ('creation_date', 'changing_date', 'client_name', 'birthday',
                  'phone_number', 'passport', 'scoring_points', 'partner',)


class OfferSerializer(serializers.HyperlinkedModelSerializer):
    credit_organization = serializers.SlugRelatedField(
        queryset=CreditOrganization.objects.all(), slug_field='username')

    class Meta:
        model = Offer
        fields = ('creation_date', 'changing_date', 'rotation_beginning_date',
                  'rotation_ending_date', 'title', 'offer_type',
                  'min_scoring_points', 'max_scoring_points',
                  'credit_organization',)
