from django.shortcuts import render
from rest_framework import generics, permissions, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from rest_framework.parsers import MultiPartParser, FormParser
from django_filters.rest_framework import DjangoFilterBackend
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
    queryset = Profile.objects.all()
    serializer_class = serializers.UserSerializer


class Get_Posts(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created')
    serializer_class = serializers.PostSerializer
    # filter_backends = [DjangoFilterBackend]

    def Post(self, serializer):
        serializer = serializers.PostSerializer(data=request.data)
        print(self)
        return ('Post was succsesful!')

        # if serializer.is_valid():
        #     serializer.save(poster=self.request.user)
        #     return('Post was succsesful!')

    # def get(self, request):
    #     post =  Post.objects.all()
    #     return Post.objects.filter(poster = User)



class Follow(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = serializers.FollowSerializer
