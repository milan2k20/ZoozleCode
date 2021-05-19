from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework.validators import UniqueValidator
from AuthAppApi.models import Users


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Users.objects.all())]
    )
    phone = PhoneNumberField(
        required=True,
        validators=[UniqueValidator(queryset=Users.objects.all())]
    )
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=Users.objects.all())]
    )
    password = serializers.CharField(
        min_length=8,
        required=True
    )

    class Meta:
        model = Users
        fields = (
            'id',
            'username',
            'email',
            'phone',
            'password')
