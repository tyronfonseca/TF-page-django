from rest_framework.serializers import ModelSerializer

from .models import Gender

class GenderSerializer(ModelSerializer):

	class Meta:
		model = Gender
		lookup_field = 'name'
		fields = ('name','gender','count','percentage')