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


import logging
logger = logging.getLogger(__name__)

# @authentication_classes((SessionAuthentication, BasicAuthentication))
# @permission_classes((IsAuthenticated,))


class ApplicationsViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    http_method_names = ['get', 'head']

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class ControlsViewSet(viewsets.ModelViewSet):
    queryset = Control.objects.all()
    serializer_class = CatalogSerializer.get_for_model(Control)
    http_method_names = ['get', 'head']

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class UnitsViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = CatalogSerializer.get_for_model(Unit)
    http_method_names = ['get', 'head']

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class BodyTypesViewSet(viewsets.ModelViewSet):
    queryset = BodyType.objects.all()
    serializer_class = CatalogSerializer.get_for_model(BodyType)
    http_method_names = ['get', 'head']

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class ControlTypesViewSet(viewsets.ModelViewSet):
    queryset = ControlType.objects.all()
    serializer_class = ControlTypeSerializer
    http_method_names = ['get', 'head']

    filter_backends = (filters.SearchFilter,)
    search_fields = ('type_name',)


class ProblemsViewSet(APIView):

    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

    def get(self, request):
        problems = Problem.objects.all()
        serializer = ProblemSerializer(problems, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        data.update(author=request.user.id)
        serializer = ProblemCreateSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            problem = serializer.save()

        read_serializer = ProblemSerializer(problem)

        return Response(read_serializer.data)


class AlertsViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    http_method_names = ['get', 'head']

    filter_backends = (filters.SearchFilter,)
    search_fields = ('application__name', 'control__name',
                     'unit__name', 'body_type__name')


class ProblemDetail(APIView):

    def get_object(self, id):
        try:
            return Problem.objects.get(pk=id)
        except Problem.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        problem = self.get_object(pk)
        serializer = ProblemSerializer(problem)
        return Response(serializer.data)


class SearchFilterView(FlatMultipleModelAPIView):
    querylist = (
        {'queryset': Application.objects.all(
        ), 'serializer_class': CatalogSerializer.get_for_model(Application)},

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
