# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from api_v1.models import Contact


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

class ContactsView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = Contact.objects.all()
        return Response(content)
