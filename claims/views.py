from claims.models import Claim, Offer, Questionnaire
from claims.serializers import (ClaimSerializer, OfferSerializer,
                                QuestionnaireSerializer)
from rest_framework import viewsets
from claims.permissions import (ClaimPermission, OfferPermission,
                                QuestionnairePermission)
from rest_framework.response import Response
# from django.views.generic.base import TemplateView


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


# class JustTest(TemplateView):
#     template_name = 'justtest.html'

#     def get_context_data(self, **kwargs):
#         context = super(JustTest, self).get_context_data(**kwargs)
#         context['debug_data'] = [self.request.user,
#                                  hasattr(self.request.user, 'creditorganization'),
#                                  hasattr(self.request.user, 'superuser'),
#                                  hasattr(self.request.user, 'partner'),
#                                  self.request.method,
#                                  ]
#         return context
