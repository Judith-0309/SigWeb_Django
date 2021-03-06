from rest_framework import serializers
from .models import Role



class RoleSerializer(serializers.Serializer):
    roles = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Role.objects.create(**validated_data)