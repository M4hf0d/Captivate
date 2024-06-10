from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'shareholders', ShareholderViewSet, basename='shareholder')
router.register(r'advisors', AdvisorViewSet, basename='advisor')
router.register(r'founders', FounderViewSet, basename='founder')
router.register(r'investors', InvestorViewSet, basename='investor')

urlpatterns = [
    path("", include(router.urls)),

    # path("groups/<int:school_id>/", GroupListView.as_view(), name="api-groups"),

]
