from rest_framework import serializers
from monitor.models import *
from rest_framework.compat import unicode_to_repr
from django.contrib.auth.models import User

import logging

logger = logging.getLogger(__name__)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'name', 'icon', 'has_controls')


class ControlTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlType
        fields = ('id', 'type_name', 'icon')


class CatalogSerializer(serializers.ModelSerializer):
    """
    A ModelSerialiser for any Catalog model with fields id, name, icon
    """
    class Meta:
        model = None
        fields = ('id', 'name', 'icon')

    @classmethod
    def get_for_model(self, model):
        self.Meta.model = model
        return self


class AlertSerializer(serializers.ModelSerializer):

    application = ApplicationSerializer()

    control = CatalogSerializer.get_for_model(
        Control)(read_only=True, many=True)

    unit = CatalogSerializer.get_for_model(
        Unit)(read_only=True, many=True)

    body_type = CatalogSerializer.get_for_model(
        BodyType)(read_only=True, many=True)

    author = UserSerializer(read_only=True)

    class Meta:
        model = Alert
        fields = ('id', 'application', 'alert_type', 'start_date',
                  'finish_date', 'category', 'control', 'unit',
                  'body_type', 'description', 'author', 'is_planed', 'is_expiered')


class ProblemSerializer(serializers.ModelSerializer):

    application = ApplicationSerializer()

    control = CatalogSerializer.get_for_model(
        Control)(read_only=True, many=True)

    unit = CatalogSerializer.get_for_model(
        Unit)(read_only=True, many=True)

    body_type = CatalogSerializer.get_for_model(
        BodyType)(read_only=True, many=True)

    author = UserSerializer(read_only=True)

    class Meta:
        model = Problem
        fields = ('id', 'status', 'detection_date', 'application', 'alert',
                  'control', 'unit', 'body_type', 'description', 'author')


class ProblemCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Problem
        fields = ('id', 'status', 'detection_date', 'application', 'alert',
                  'control', 'unit', 'body_type', 'description', 'author')

    def create(self, validated_data):

        logger.error(validated_data)

        application = validated_data.get('application')
        control = validated_data.get('control')
        unit = validated_data.get('unit')
        body_type = validated_data.get('body_type')
        description = validated_data.get('description')
        author = validated_data.get('author')

        problem = Problem.objects.create(
            application=application,
            description=description,
            author=author
        )

        problem.control.set(control)
        problem.unit.set(unit)
        problem.body_type.set(body_type)

        if (validated_data.get('detection_date') is not None):
            problem.detection_date = validated_data.get('detection_date')

        return problem
