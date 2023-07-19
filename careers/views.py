from .models import Careers
from .serializers import CareersSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.urlpatterns import format_suffix_patterns


@api_view(['GET', 'POST']) 
def careers_list(request):

    if request.method == 'GET':
        careers = Careers.objects.all()
        serializer = CareersSerializer(careers, many =True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer =CareersSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
       

@api_view(['GET','PUT','DELETE']) 
def careers_detail(request,id):
    try:
        careers=Careers.objects.get(pk=id)
    except Careers.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)       

    if request.method == 'GET':
           serializer = CareersSerializer(careers)
           return Response(serializer.data)
    elif request.method == 'PUT':
         serializer = CareersSerializer(careers,data= request.data)
         if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method =='DELETE':
        careers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)