from rest_framework import serializers
from .models import Asset2

class   AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset2
        fields = '__all__'