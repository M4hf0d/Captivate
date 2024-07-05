from rest_framework import viewsets
from .models import *
from .serializers import *


class DomainViewSet(viewsets.ModelViewSet):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer