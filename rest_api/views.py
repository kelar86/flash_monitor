from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated

import json
from rest_framework import viewsets
from monitor.models import *
from .models import *
from .serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters
from django_filters import FilterSet
from drf_multiple_model.views import ObjectMultipleModelAPIView, FlatMultipleModelAPIView


# @authentication_classes((SessionAuthentication, BasicAuthentication))
# @permission_classes((IsAuthenticated,))
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


class SearchFilterView(FlatMultipleModelAPIView):
    querylist = (
        {'queryset': Application.objects.all(
        ), 'serializer_class': ApplicationSearchSerializer},

        {'queryset': Control.objects.all(), 'serializer_class': CatalogSerializer.get_for_model(
            Control)},
        {'queryset': Unit.objects.all(), 'serializer_class': CatalogSerializer.get_for_model(
            Unit)},
        {'queryset': BodyType.objects.all(), 'serializer_class': CatalogSerializer.get_for_model(
            BodyType)}
    )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class AdviseSearchView(APIView):
    def get(self, request):
        search = SearchAdvise.objects.get(pk=1)
        return Response(json.loads(search.schema))
