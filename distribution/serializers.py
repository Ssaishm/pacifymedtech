from . import models
from rest_framework import serializers
from rest_framework.fields import CharField, EmailField



class disContactSerializer(serializers.ModelSerializer):

	title = CharField( required=False)
	description= CharField( required=False)
	personalname = CharField(required=True)
	personalemail = EmailField(required=True)
	personalphone = CharField(required =True)
	companyname = CharField( required=True)
	companyemail = EmailField(required=True)
	companyurl= CharField(required=True)
	companycity= CharField(required=True)
	companystate= CharField(required=True)
	companyzipcode= CharField(required=True)
	companyaddress= CharField(required=True)
	#experience
	designation=CharField(required=True)
	industry=CharField(required=True)
	years=CharField(required=True)
	question=CharField(required=True)
	speciality=CharField(required=True)

	class Meta:
		model = models.disContact
		fields = (
			'title',
			'description',
			'personalname',
			'personalemail',
			'personalphone',
			'companyname',
			'companyemail',
			'companyurl',
			'companycity',
			'companystate',
			'companyzipcode',
			'companyaddress',
			'designation',
			'industry',
			'years',
			'question',
			'speciality',
		)