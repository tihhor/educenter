from django.conf.urls import include
from .models import Subject, Result, Person
from rest_framework import routers, serializers, viewsets


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class ResultSerializer(serializers.HyperlinkedModelSerializer):
    # result = serializers.HyperlinkedRelatedField(many=True, view_name='result-detail', read_only=True)
    class Meta:
        model = Result
        fields = ['person', 'subject', 'mark']
        # lookup_field = 'mark'
        # extra_kwargs = {
        #     'url': {'lookup_field': 'mark'}
        # }

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
