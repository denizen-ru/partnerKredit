from claims.models import Claim, Offer, Questionnaire
from claims.serializers import (ClaimSerializer, OfferSerializer,
                                QuestionnaireSerializer)
from rest_framework import viewsets
from claims.permissions import (ClaimPermission, OfferPermission,
                                QuestionnairePermission)
from rest_framework.response import Response


class ClaimsViewSet(viewsets.ModelViewSet):
    """
    This viewset provides `list`, `create`, `retrieve`, `update`
    and `destroy` actions for model Claims.
    """
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer
    permission_classes = (ClaimPermission,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = 'SENT'
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class OffersViewSet(viewsets.ModelViewSet):
    """
    This viewset provides `list`, `create`, `retrieve`, `update`
    and `destroy` actions for model Offers.
    """
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = (OfferPermission,)


class QuestionnairesViewSet(viewsets.ModelViewSet):
    """
    This viewset provides `list`, `create`, `retrieve`, `update`
    and `destroy` actions for model Questionnaires.
    """
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer
    permission_classes = (QuestionnairePermission,)
