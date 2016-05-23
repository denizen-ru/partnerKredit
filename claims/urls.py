from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from claims import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'claims', views.ClaimsViewSet)
router.register(r'offers', views.OffersViewSet)
router.register(r'questionnaires', views.QuestionnairesViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    # url(r'^justtest/$', views.JustTest.as_view()),
    url(r'^', include(router.urls)),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework'))
]
