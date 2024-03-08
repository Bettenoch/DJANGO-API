from rest_framework import serializers

class AbstractSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source='public_id', readonly=True, format='hex')
    created = serializers.DateTimeField(readonly=True)
    updated = serializers.DateTimeField(readonly=True)