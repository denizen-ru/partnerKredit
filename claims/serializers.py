from rest_framework import serializers
from claims.models import Claim, Questionnaire, Offer
from accounts.models import Partner, CreditOrganization


class ClaimSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Claim
        fields = ('creation_date', 'sending_date',
                  'questionnaire', 'offer', 'status')


# class PartnerSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Partner
#         fields = ('user',)


class QuestionnaireSerializer(serializers.HyperlinkedModelSerializer):
    # partners = serializers.HyperlinkedIdentityField(view_name='partner-list')
    # partners = serializers.StringRelatedField(many=True)
    # partners = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    # partners = PartnerSerializer(many=True, read_only=True)
    # partner_name = serializers.RelatedField(source='partner', read_only=True)
    partner_name = serializers.ReadOnlyField(source='partner')

    class Meta:
        model = Questionnaire
        fields = ('creation_date', 'changing_date', 'client_name', 'birthday',
                  'phone_number', 'passport', 'scoring_points',  #'partner',
                  'partner_name')


class OfferSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Offer
        fields = ('creation_date', 'changing_date', 'rotation_beginning_date',
                  'rotation_ending_date', 'title', 'offer_type',
                  'min_scoring_points', 'max_scoring_points',
                  'credit_organization')
