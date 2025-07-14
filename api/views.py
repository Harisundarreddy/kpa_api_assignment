from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import KPAFormData
from api.serializers import KPAFormDataSerializer



# Create your views here.


class FormDataView(APIView):
    def post(self,request):
        ser = KPAFormDataSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'message': 'Form data saved', 'data': ser.data}, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def get(self,request,pk=None):
        try:
            data = KPAFormData.objects.get(id=pk)
            ser = KPAFormDataSerializer(data)
            return Response(ser.data)
        except KPAFormData.DoesNotExist:
            return Response({'error': 'Data not found'}, status=status.HTTP_404_NOT_FOUND)