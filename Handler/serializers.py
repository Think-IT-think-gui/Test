from rest_framework import serializers
from . models import SignUp_info
class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUp_info
        fields = '__all__'