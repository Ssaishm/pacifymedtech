from .models import Home
from .models import Hblogs
from .models import HImage
from .models import HLogo
from .serializers import HomeSerializer
from .serializers import HblogsSerializer
from .serializers import HImageSerializer
from .serializers import HLogoSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.urlpatterns import format_suffix_patterns
from django.shortcuts import render
from django.http import Http404


@api_view(['GET', 'POST'])
def home_list(request):

    if request.method == 'GET':
        home= Home.objects.all()
        serializer = HomeSerializer(home, many =True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer =HomeSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def home_detail(request,id):
    try:
        home=Home.objects.get(pk=id)
    except Home.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
           serializer = HomeSerializer(home)
           return Response(serializer.data)
    elif request.method == 'PUT':
         serializer = HomeSerializer(home,data= request.data)
         if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method =='DELETE':
        home.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def hblogs_list(request):

    if request.method == 'GET':
        hblogs= Hblogs.objects.all()
        serializer = HblogsSerializer(hblogs, many =True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer =HblogsSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def hblogs_detail(request,id):
    try:
        hblogs=Hblogs.objects.get(pk=id)
    except Home.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
           serializer = HblogsSerializer(hblogs)
           return Response(serializer.data)
    elif request.method == 'PUT':
         serializer = HblogsSerializer(hblogs,data= request.data)
         if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method =='DELETE':
        hblogs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def home_list(request):

    if request.method == 'GET':
        home= Home.objects.all()
        serializer = HomeSerializer(home, many =True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer =HomeSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def home_detail(request,id):
    try:
        home=Home.objects.get(pk=id)
    except Home.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
           serializer = HomeSerializer(home)
           return Response(serializer.data)
    elif request.method == 'PUT':
         serializer = HomeSerializer(home,data= request.data)
         if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method =='DELETE':
        home.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def hImage_list(request):

    if request.method == 'GET':
        hImage= HImage.objects.all()
        serializer = HImageSerializer(hImage, many =True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer =HImageSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)




@api_view(['GET','PUT','DELETE'])
def hImage_detail(request,id):
    try:
        hImage=HImage.objects.get(pk=id)#######
    except HImage.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
           serializer = HImageSerializer(hImage)
           return Response(serializer.data)
    elif request.method == 'PUT':
         serializer = HImageSerializer(hImage,data= request.data)
         if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method =='DELETE':
        hImage.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def hLogo_list(request):

    if request.method == 'GET':
        hLogo= HLogo.objects.all()
        serializer = HLogoSerializer(hLogo, many =True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer =HLogoSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def hLogo_detail(request,id):
    try:
        hLogo=HLogo.objects.get(pk=id)#######
    except HLogo.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
           serializer = HLogoSerializer(hLogo)
           return Response(serializer.data)
    elif request.method == 'PUT':
         serializer = HLogoSerializer(hLogo,data= request.data)
         if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method =='DELETE':
        hLogo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)