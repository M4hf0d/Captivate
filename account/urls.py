from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'Advisings', AdvisingViewSet, basename='Advising')
router.register(r'Foundings', FoundingViewSet, basename='Founding')
router.register(r'Investings', InvestingViewSet, basename='Investing')

urlpatterns = [
    path("", include(router.urls)),

    # path("groups/<int:school_id>/", GroupListView.as_view(), name="api-groups"),

]
