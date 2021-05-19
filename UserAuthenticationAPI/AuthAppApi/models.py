from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class Users(AbstractUser):
    phone = PhoneNumberField()
