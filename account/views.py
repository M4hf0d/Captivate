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


class ShareholderViewSet(viewsets.ModelViewSet):

    filter_backends = [DjangoFilterBackend]
    # filterset_fields = [""]
    queryset = Shareholder.objects.all()
    def get_serializer_class(self):
        if (
            self.request.method == "POST"
            or self.request.method == "PUT"
            or self.request.method == "PATCH"
        ):
            return ShareholderSerializer
        return ShareholderListSerializer



class AdvisorViewSet(viewsets.ModelViewSet):

    filter_backends = [DjangoFilterBackend]
    # filterset_fields = [""]
    queryset = Advisor.objects.all()

    def get_serializer_class(self):
        if (
            self.request.method == "POST"
            or self.request.method == "PUT"
            or self.request.method == "PATCH"
        ):
            return AdvisorSerializer
        return AdvisorListSerializer
    
    
class FounderViewSet(viewsets.ModelViewSet):

    filter_backends = [DjangoFilterBackend]
    # filterset_fields = [""]
    queryset = Founder.objects.all()

    def get_serializer_class(self):
        if (
            self.request.method == "POST"
            or self.request.method == "PUT"
            or self.request.method == "PATCH"
        ):
            return FounderSerializer
        return FounderListSerializer


    
class InvestorViewSet(viewsets.ModelViewSet):

    filter_backends = [DjangoFilterBackend]
    # filterset_fields = [""]
    queryset = Investor.objects.all()
    def get_serializer_class(self):
        if (
            self.request.method == "POST"
            or self.request.method == "PUT"
            or self.request.method == "PATCH"
        ):
            return InvestorSerializer
        return InvestorListSerializer
