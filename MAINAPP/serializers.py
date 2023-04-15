from rest_framework import serializers
from MAINAPP.models import UserInfo
class UserSerializer(serializers.ModelSerializer):
    class Meta():
        fields = '__all__'
        model = UserInfo