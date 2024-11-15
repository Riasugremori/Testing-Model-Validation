from rest_framework import serializers
from .models import *

class DeliveryProofSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryProof
        fields = '__all__'  