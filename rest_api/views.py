from rest_framework import viewsets
from monitor.models import *
from .serializers import *


class ApplicationsViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    http_method_names = ['get', 'head']


class ProblemsViewSet(viewsets.ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ApplicationSerializer
    http_method_names = ['get', 'head']


class AlertsViewSet(viewsets.ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ApplicationSerializer
    http_method_names = ['get', 'head']
