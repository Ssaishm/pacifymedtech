
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from .models import Careers
from rest_framework.fields import CharField




class CareersSerializer(serializers.ModelSerializer):
    name = CharField( required=True)
    details = CharField( required=True)
    location= CharField(required =True)






    class Meta:
        model =Careers
        
        fields =('id','name','details','location')