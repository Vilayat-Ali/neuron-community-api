from rest_framework import serializers

class important_problem(serializers.Serializer):
    full_name = serializers.CharField(max_length=25)
    email = serializers.EmailField(max_length=50)
    description = serializers.CharField(max_length=300)