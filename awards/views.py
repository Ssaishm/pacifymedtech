from django.shortcuts import render
from awards.models import Awards
from awards.models import AImage
from django.http import Http404
from .serializers import AwardsSerializer
from .serializers import AImageSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.urlpatterns import format_suffix_patterns


@api_view(['GET', 'POST'])
def awards_list(request):

    if request.method == 'GET':
        awards= Awards.objects.all()
        serializer = AwardsSerializer(awards, many =True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer =AwardsSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def awards_detail(request,id):
    try:
        awards=Awards.objects.get(pk=id)
    except Awards.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
           serializer =AwardsSerializer(awards)
           return Response(serializer.data)
    elif request.method == 'PUT':
         serializer =AwardsSerializer(awards,data= request.data)
         if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method =='DELETE':
        awards.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    ############################

@api_view(['GET', 'POST'])
def AImage_list(request):

    if request.method == 'GET':
        hImage= AImage.objects.all()
        serializer = AImageSerializer(hImage, many =True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer =AImageSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def AImage_detail(request,id):
    try:
        aImage=AImage.objects.get(pk=id)#######
    except AImage.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
           serializer = AImageSerializer(aImage)
           return Response(serializer.data)
    elif request.method == 'PUT':
         serializer = AImageSerializer(aImage,data= request.data)
         if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method =='DELETE':
        aImage.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





