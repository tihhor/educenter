from django.conf.urls import include
from .models import Subject, Result, Person, Group
from rest_framework import routers, serializers, viewsets


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class ResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Result
        fields = ['person', 'subject', 'mark']


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    person = serializers.StringRelatedField(many=True)
    class Meta:
        model = Group
        fields = ['name', 'person']