from rest_framework import serializers
from core.user.models import User

class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source='public_id', readonly=True, format='hex')
    created = serializers.DateTimeField(readonly=True)
    updated = serializers.DateTimeField(readonly=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'bio', 'avatar', 'is_active', 'created', 'updated']
        read_only_field = ['is_active']