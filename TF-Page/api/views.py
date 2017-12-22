# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404 #si no existe retorna un 404
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView,CreateAPIView,DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Gender
from .serializers import GenderSerializer


class GenderNameList(APIView):

	def get(self, resquest):
		queryset = Gender.objects.all()
		serializer = GenderSerializer(queryset, many=True)
		return Response(serializer.data)

	def post(self):
		pass 

class GetGenderName(RetrieveAPIView):
	serializer_class = GenderSerializer
	lookup_field = 'name'
	def get_queryset(self):
		name = self.kwargs['name']
		return Gender.objects.filter(name=name)

class CreateGenderName(CreateAPIView):
	queryset = Gender.objects.all()
	serializer_class = GenderSerializer

class DeleteGenderName(DestroyAPIView):
	queryset = Gender.objects.all()
	serializer_class = GenderSerializer	

			