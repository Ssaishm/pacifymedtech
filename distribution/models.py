from django.db import models
from utils.model_abstracts import Model
from django_extensions.db.models import (
	TimeStampedModel,
	ActivatorModel,
	TitleDescriptionModel
)

class disContact(
	TimeStampedModel,
	ActivatorModel,
	TitleDescriptionModel,
	Model
	):

	class Meta:
		verbose_name_plural = "disContacts"

	#personalname = models.CharField(blank=True, null=True,max_length=255,verbose_name="Personalname")
	title = models.CharField(max_length=100, blank=True,null =True, default='')
	description= models.TextField(max_length=100,blank=True,null=True, default =' ')
	personalname= models.CharField(blank=False, null=True,max_length=255,verbose_name= "personalname")
	#message= models.TextField(max_length=100,blank=True, default =' ')
	personalemail = models.EmailField(blank=False, null=True,max_length=255,verbose_name="personalemail")
	personalphone= models.CharField(blank=False, null=True,max_length=255,verbose_name= "personalphone")
	companyname = models.CharField(blank=False, null=True,max_length=255,verbose_name="companyname")
	companyemail = models.EmailField(blank=False, null=True,max_length=255,verbose_name="companyemail")
	companyurl = models.CharField(blank=False, null=True,max_length=255,verbose_name="companyurl")
	companycity = models.CharField(blank=False, null=True,max_length=255,verbose_name="companycity")
	companystate = models.CharField(blank=False, null=True,max_length=255,verbose_name="companystate")
	companyzipcode = models.CharField(blank=False, null=True,max_length=255,verbose_name="companyzipcode")
	companyaddress= models.TextField(blank=False, null=True,max_length=1000,verbose_name="companyaddress")
	designation = models.CharField(blank=False, null=True,max_length=255,verbose_name="designation")
	industry = models.CharField(blank=False, null=True,max_length=255,verbose_name="industry")
	years = models.CharField(blank=False, null=True,max_length=255,verbose_name="years")
	question = models.CharField(blank=False, null=True,max_length=255,verbose_name="question")
	speciality = models.CharField(blank=False, null=True,max_length=255,verbose_name="speciality")
	######################


	def __str__(self):
		return f'{self.title}'