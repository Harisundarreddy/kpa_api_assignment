from rest_framework import serializers
from .models import KPAFormData

class KPAFormDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = KPAFormData
        fields = '__all__'
