from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from .models import Awards
from .models import AImage
from rest_framework.fields import CharField




class AwardsSerializer(serializers.ModelSerializer):
    title = CharField( required=True)
    details= CharField( required=True)
    
  
    class Meta:
        model =Awards
        
        fields =('id','title','details')


class AImageSerializer(serializers.ModelSerializer):
    name = CharField( required=True)
    image = CharField(required =True)
    
  
    class Meta:
        model =AImage
        
        fields =('id','name','image')