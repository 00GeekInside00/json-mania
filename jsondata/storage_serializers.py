from rest_framework import serializers
from .models import Storage

class StorageSerializer(serializers.ModelSerializer):
    data = serializers.JSONField()
    class Meta:
        model = Storage
        fields=("data",)
      

class StorageWriteSerializer(serializers.ModelSerializer):
    data = serializers.JSONField()
    class Meta:
        model = Storage
        exclude=('id',)
