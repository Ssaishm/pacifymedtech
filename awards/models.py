from django.db import models
from utils.model_abstracts import Model
from django_extensions.db.models import (
	TimeStampedModel,
	ActivatorModel,
	TitleDescriptionModel
)


class Awards(models.Model):

    title =models.CharField(max_length=200)
    details = models.TextField(blank=False, null=True,max_length=500,verbose_name="Details")


    class Meta:
        verbose_name_plural = "Awards"

    def __str__(self):
        return self.title + ' ' + self.details

class AImage(models.Model):
    name= models.CharField(max_length=200)
    image =models.CharField(blank=False,default='Add image url here',null=True,max_length=100)

    class Meta:
        verbose_name_plural ="AwardsImages"

    def __str__(self):
        return self.name + ' ' + self.image


    
    
