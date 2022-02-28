from rest_framework import serializers

class projectSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=150)
    image = serializers.CharField(max_length=200)
    postedAt = serializers.DateField()
    description = serializers.CharField()
    tags = serializers.JSONField()
