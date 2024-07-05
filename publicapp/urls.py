from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
    openapi.Info(
        title="Captivate APi",
        default_version="v1",
        description="Captivate API Documentation",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)



router = DefaultRouter()
router.register(r'domains', DomainViewSet)



urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("", include("account.urls")),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)