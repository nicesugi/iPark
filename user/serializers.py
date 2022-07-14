from rest_framework import serializers
import re

from user.models import User as UserModel


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserModel
        fields = ["username", "password", "fullname", "email", "phone", "birthday", "region", "join_date"]
        
        extra_kwargs = {
            "password": {"write_only": True},
        }
        