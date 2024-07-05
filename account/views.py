from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from django_filters.rest_framework import DjangoFilterBackend


from .models import *
from .serializers import *





class AdvisingViewSet(viewsets.ModelViewSet):

    filter_backends = [DjangoFilterBackend]
    # filterset_fields = [""]
    queryset = Advising.objects.all()

    def get_serializer_class(self):
        if (
            self.request.method == "POST"
            or self.request.method == "PUT"
            or self.request.method == "PATCH"
        ):
            return AdvisingSerializer
        return AdvisingListSerializer
    
    
class FoundingViewSet(viewsets.ModelViewSet):

    filter_backends = [DjangoFilterBackend]
    # filterset_fields = [""]
    queryset = Founding.objects.all()

    def get_serializer_class(self):
        if (
            self.request.method == "POST"
            or self.request.method == "PUT"
            or self.request.method == "PATCH"
        ):
            return FoundingSerializer
        return FoundingListSerializer


    
class InvestingViewSet(viewsets.ModelViewSet):

    filter_backends = [DjangoFilterBackend]
    # filterset_fields = [""]
    queryset = Investing.objects.all()
    def get_serializer_class(self):
        if (
            self.request.method == "POST"
            or self.request.method == "PUT"
            or self.request.method == "PATCH"
        ):
            return InvestingSerializer
        return InvestingListSerializer
