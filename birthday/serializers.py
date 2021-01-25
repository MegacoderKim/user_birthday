from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import UserBirthday


class UserBirthdaySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBirthday
        fields = ["id", "first_name", "last_name", "email", "birthday"]

        def validate(self, data):
            print(data)
