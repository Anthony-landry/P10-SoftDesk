from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from account.models import Contributor


User = get_user_model()


class UserRegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'age', 'password', 'can_be_contacted', 'can_data_be_shared')

        extra_kwargs = {'password': {
            # Permet de cacher le password, si on possède la liste des utilisateurs avec une méthode GET
            'write_only': True,
            'required': True,
            # Permet de cacher le password dans le champ Password ( de base le mot de passe est en clair)
            "style": {'input_type': 'password'},
        }
        }

    @staticmethod
    def validate_password(value):
        try:
            validate_password(value)
        except ValidationError as exc:
            raise serializers.ValidationError(str(exc))
        return value

    def create(self, validated_data):

        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        if 'password' in validated_data:
            user.set_password(validated_data['password'])
            user.save()
        return user


class ContributorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = "__all__"
