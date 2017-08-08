# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from models import Message
from django.contrib.auth import models as auth_models
from django.shortcuts import get_object_or_404
from serializers import MessageSerializer, UserSerializer
from rest_framework import viewsets, permissions
from rest_framework.response import Response


class UserView(viewsets.ModelViewSet):
    queryset = auth_models.User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs['pk']
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class MessageView(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.AllowAny]
