# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import json
from collections import Counter
# Create your models here.

GENEROS = (
    ("m", "Masculino"),
    ("f", "Femenino"))

class Gender(models.Model):
	name = models.CharField(max_length=30)
	gender = models.CharField(max_length=1,choices=GENEROS)
	count = models.IntegerField()
	percentage = models.FloatField()

	def __str__(self):
		return self.name
#==========================================
# Modelo para guardar paginas de facebook
#==========================================
class PagesModel(models.Model):
	fb_id = models.IntegerField(unique=True, db_index=True, primary_key=True)
	likes = models.IntegerField()
	name = models.CharField(max_length=124)
	
	def __str__(self):
		return self.name
#==========================================
# Modelo de likes por dia
#==========================================
class LikesPerDay(models.Model):
	fb_id = models.ForeignKey(PagesModel, related_name='likesperday') 
	date = models.DateField()
	number_likes = models.IntegerField()
	
	def __str__(self):
		for e in PagesModel.objects.filter(name = self.fb_id):
			return '{0} - FECHA: {1}'.format(e.name, self.date)
		
#==========================================
# Modelo de los post
#==========================================
class PostsModel(models.Model):
	fb_id = models.ForeignKey(PagesModel, related_name='posts')
	post_id = models.IntegerField()
	post_type = models.CharField(max_length=30)
	reactions = models.TextField() #JSON FORMAT
	comments = models.TextField() #JSON FORMAT
	
	
	def __str__(self):
		for e in PagesModel.objects.filter(name = self.fb_id):
			return '{0} - ID_POST: {1}'.format(e.name, self.post_id)

	@property
	def typeReactionHandler(self):
		n = json.loads(self.reactions)

		lista = jsonToList(n,'type')

		type = dict(Counter(lista))
		return type
	
	@property
	def genderReactionHandler(self):
		n = json.loads(self.reactions)

		lista = jsonToList(n,'name')
		generos = []

		for fullname in lista:
			namelist = fullname.split(" ")
			try:
				result = Gender.objects.get(name = namelist[0])
				gender = result.gender
			except Gender.DoesNotExist:
				gender = "nil"	

			generos.append(gender)

		return dict(Counter(generos))			
		
#==========================================
# Tomar un json objet y returnar una lista 
# con los valores del campo especificado en
# @value = 'name' or 'type'
#==========================================		
def jsonToList(lista,value):
	data = []
	for item in lista:
		c = json.dumps(item[value], indent = 2, separators=(',',': '))
		c = c.replace('"', '')
		data.append(c)
	return data

		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
	