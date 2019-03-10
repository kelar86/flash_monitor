from rest_framework import viewsets
from monitor.models import *
from .serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from itertools import chain
from rest_framework import filters
from django_filters import FilterSet
from drf_multiple_model.views import ObjectMultipleModelAPIView


class ApplicationsViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    http_method_names = ['get', 'head']


class ProblemsViewSet(viewsets.ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    http_method_names = ['get', 'head']


class AlertsViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    http_method_names = ['get', 'head']


class ProblemDetail(APIView):

    def get_object(self, id):
        try:
            return Problem.objects.get(pk=id)
        except Problem.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        problem = self.get_object(id)
        serializer = ProblemSerializer(problem)
        return Response(serializer.data)


class SearchFilterView(ObjectMultipleModelAPIView):
    querylist = (
        {'queryset': Application.objects.all(
        ), 'serializer_class': ApplicationSearchSerializer},
        {'queryset': Control.objects.all(), 'serializer_class': ControlSearchSerializer},
        {'queryset': Unit.objects.all(), 'serializer_class': UnitSearchSerializer},
        {'queryset': BodyType.objects.all(), 'serializer_class': BodyTypeSearchSerializer}
    )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
