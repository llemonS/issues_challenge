from django.shortcuts import render

from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .serializers import IssueSerializer

from .models import Issue

class IssueView(ModelViewSet):
    """
    View responsible for Issue model basic CRUD operations.
    """
    serializer_class = IssueSerializer
    permission_classes = (AllowAny,)
    queryset = Issue.objects.all()

    def create(self, request, *args, **kwargs):
        print(f"Issue created: {request.data}")
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        print(f"Issue updated: {request.data}")
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        print(f"Issue deleted: {request.data}")
        return super().destroy(request, *args, **kwargs)
