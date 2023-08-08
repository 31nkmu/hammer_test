from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import random

from applications.account.manager import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    phone_number = PhoneNumberField(unique=True)
    password = models.CharField(max_length=120)
    invite_code = models.CharField(max_length=6, blank=True, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    parent = models.ForeignKey("CustomUser", on_delete=models.CASCADE, related_name='children', null=True, blank=True)

    @staticmethod
    def create_password():
        random_num = random.choices(range(10), k=4)
        return ''.join(str(num) for num in random_num)

    def create_invite_code(self):
        import string
        let_nums = string.ascii_letters + ''.join(str(num) for num in range(10))
        random_code = random.choices(let_nums, k=6)
        self.invite_code = ''.join(random_code)

    def __str__(self):
        return str(self.phone_number)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
