from django.db import models
from utils.model_abstracts import Model
from django_extensions.db.models import (
	TimeStampedModel, 
	ActivatorModel,
	TitleDescriptionModel
)

class DemoContact(
	TimeStampedModel, 
	ActivatorModel,
	TitleDescriptionModel,
	Model
	):

	class Meta:
		verbose_name_plural = "DemoContacts"

	
	organization = models.CharField( blank=False, null= True,max_length=255, verbose_name='organization')
	number = models.CharField(blank=False, null= True,max_length=13, verbose_name='number')
	email = models.EmailField(verbose_name="Email")

	def __str__(self):
		return f'{self.title}'