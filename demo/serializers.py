from . import models
from rest_framework import serializers
from rest_framework.fields import CharField, EmailField



class DemoContactSerializer(serializers.ModelSerializer):

	name = CharField(source="title", required=True)
	message = CharField(source="description", required=True)
	email = EmailField(required=True)
	number = CharField(required= True)
	organization = CharField(required= True)

	
	class Meta:
		model = models.DemoContact
		fields = (
			'name',
			'number',
			'organization',
			'message',
			'email',	
		)