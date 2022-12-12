from .models import Subject, Result, Person, Group
from .serializers import SubjectSerializer, ResultSerializer, PersonSerializer, GroupSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import ReadOnly, IsActive
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication

class SubjectViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser|ReadOnly]
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class ResultViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser | IsActive | ReadOnly]
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

class PersonViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication, SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.prefetch_related('person')
    serializer_class = GroupSerializer
