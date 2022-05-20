from rest_framework import serializers
from .models import Message
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email')

class MessageSerializer(serializers.ModelSerializer):
    created_by = UserSerializer()
    class Meta:
        model = Message
        fields = ('__all__')
