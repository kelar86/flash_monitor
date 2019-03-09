from rest_framework import serializers
from monitor.models import *


class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'name', 'icon', 'has_controls', 'is_visiable')


class ProblemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Problem
        fields = ('id', 'status', 'icon',
                  'detection_date', 'application', 'alert', 'control', 'unit',
                  'body_type', 'description', 'author')


class AletrtSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alert
        fields = ('id', 'alert_type', 'start_date',
                  'finish_date', 'category', 'control', 'unit',
                  'body_type', 'description', 'author')
