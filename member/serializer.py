from rest_framework import serializers

class memberSerializer(serializers.Serializer):
    image = serializers.CharField(max_length=100, default="https://bootdey.com/img/Content/avatar/avatar1.png")
    full_name = serializers.CharField(max_length=100, required=True)
    role = serializers.CharField(max_length=100, required=True)
    github = serializers.CharField(max_length=100, required=False, default=None)
    linkedin = serializers.CharField(max_length=100, required=False, default=None)
    twitter = serializers.CharField(max_length=100, required=False, default=None)
