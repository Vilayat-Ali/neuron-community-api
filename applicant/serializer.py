from rest_framework import serializers

class applicantSerializer(serializers.Serializer):
    fll_name = serializers.CharField(max_length=100, required=False)
    email = serializers.EmailField(max_length=100, required=False)
    phone = serializers.CharField(max_length=15, required=False) 
    description = serializers.CharField(max_length=400)  