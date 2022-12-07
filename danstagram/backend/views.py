from django.shortcuts import render
from rest_framework import generics, permissions, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *

from . import models
from . import serializers

class UserListView(generics.ListAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.UserSerializer

class UserCreate(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request, format='json'):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Get_Profile(viewsets.ModelViewSet):
    # permission_classes = (permissions.AllowAny)
    queryset = Profile.objects.all()
    serializer_class = serializers.UserSerializer
