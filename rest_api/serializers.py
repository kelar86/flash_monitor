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
                  'body_type', 'description', 'author', 'is_planed')


class ApplicationSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'name', 'icon')


class ControlSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Control
        fields = ('id', 'name', 'icon')


class UnitSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ('id', 'name', 'icon')


class BodyTypeSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyType
        fields = ('id', 'name', 'icon')
