from rest_framework import serializers
from monitor.models import *


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'name', 'icon', 'has_controls', 'is_visiable')


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ('id', 'status', 'detection_date', 'application', 'alert',
                  'control', 'unit', 'body_type', 'description', 'author')


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ('id', 'alert_type', 'start_date',
                  'finish_date', 'category', 'control', 'unit',
                  'body_type', 'description', 'author')


class ApplicationSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'name')


class ControlSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Control
        fields = ('id', 'name')


class UnitSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ('id', 'name')


class BodyTypeSearchSerializer(serializers.ModelSerializer):
    class Meta:
        models = BodyType
        fields = ('id', 'name')
