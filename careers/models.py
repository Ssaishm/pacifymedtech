from django.db import models
from utils.model_abstracts import Model
from django_extensions.db.models import (
	TimeStampedModel,
	ActivatorModel,
	TitleDescriptionModel
)

class Careers(models.Model):

    name =models.CharField(max_length=50)
    details = models.TextField(max_length=6000)
    location = models.CharField(default= 'Mumbai',max_length=200)


    class Meta:
        verbose_name_plural = "Careers"

    def __str__(self):
        return self.name + ' ' + self.details +' ' + self.location


