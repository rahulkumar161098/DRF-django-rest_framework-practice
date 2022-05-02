
from gc import get_objects
from itertools import product
from django.shortcuts import render
from app import serializer
# from app.serializer import ProductSerializer
from django.http import JsonResponse
from app.models import Product, ProductSerializer
from rest_framework.parsers import JSONParser    # convert json to dict
from django.views.decorators.csrf import csrf_exempt   #disable csrf validations
from django.utils.decorators import method_decorator     # method decorator for csrf token
from rest_framework.decorators import api_view
from rest_framework.response import Response    # response in api views
from rest_framework import status   #raise errors
from rest_framework.views import APIView   #for class views
from django.http import Http404   # raise http404 error

# Create your views here.
# @method_decorator(csrf_exempt)

# @api_view(['GET', 'POST'])
# def products(request):
#     if request.method== 'GET':
#         Plist= Product.objects.all()
#         serializer= ProductSerializer(Plist, many=True)
#         # return Response(serializer.data, safe=False)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     if request.method == 'POST':
#         # json_data= JSONParser().parse(request)
#         serializer= ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         # return JsonResponse(serializer.errors, safe=True)
#         return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

# @method_decorator(csrf_exempt)\

# @api_view(['GET', 'PUT', 'DELETE'])
# def productById(request, id):
#     try:
#         Plist=Product.objects.get(pk=id)
#     except Product.DoesNotExist:
#         return Response(status=status.HTTP_403_FORBIDDEN)

#     if request.method == 'GET':
#         serialize= ProductSerializer(Plist)
#         return Response(serialize.data)

#     elif request.method=='PUT':
#         # json_data= JSONParser().parse(request)
#         serialize= ProductSerializer(Plist, data= request.data)
#         if serialize.is_valid():
#             serialize.save()
#             return Response(serialize.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#     elif request.method=='DELETE':
#         Plist.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)


#
# class based views
class viewProduct(APIView):
    def get(self, request, format=None):
        json_data= Product.objects.all()
        serializer= ProductSerializer(json_data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer= ProductSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response (status=status.HTTP_403_FORBIDDEN)

class productById(APIView):
    def get_object(self, id):
        try:
            return Product.objects.get(pk=id)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        product = self.get_object(id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, id):
        product= self.get_object(id)
        serializer= ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        raise Http404

    def delete(self, request, id):
        product= self.get_object(id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



