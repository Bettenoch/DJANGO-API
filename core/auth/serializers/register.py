from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from core.user.serializers import UserSerializer
from core.user.models import User

class RegisterSerializer(UserSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'bio', 'avatar', 'password']
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
    