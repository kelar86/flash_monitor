from rest_framework import serializers
from monitor.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'name', 'icon', 'has_controls')


class ApplicationSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = ('id', 'name', 'icon')


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
