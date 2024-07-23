from django.shortcuts import render
from rest_framework. views import APIView
from .serializer import PesronModelSerializer
from . models import Person
from rest_framework.response import Response

# Create your views here.


class PersonClassview(APIView):

    def get(self,request):
        data=Person.objects.all()
        serializer=PesronModelSerializer(data,many=True)
        return Response(serializer.data)
    


    def post(self,request):
        serializer=PesronModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'DATA ADDED ....'})



    def put(self,request):
        pk =request.data['id']
        print(pk)
        obj=Person.objects.get(id=pk)
        serializer=PesronModelSerializer(obj,data=request.data,partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"PUT UPDATE COMPLETED"})



    def patch(self,request):
        pk =request.data['id']
        obj=Person.objects.get(id=pk)
        serializer=PesronModelSerializer(obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"PATCH UPDATE COMPLETED"})



    def delete(self,request):
        pk=request.data['id']
        data=Person.objects.get(id=pk)
        data.delete()
        return Response({"msg":"data deleted !!!"})

