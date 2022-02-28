from rest_framework import serializers

class newSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=400)
    issuer = serializers.CharField(max_length=150)
    links = serializers.JSONField()
    date = serializers.DateField()