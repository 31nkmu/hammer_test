import time

from django.contrib.auth import get_user_model
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField

User = get_user_model()


class UserSerializer(serializers.Serializer):
    phone_number = PhoneNumberField()
    invite_code = serializers.CharField(max_length=6)


class AuthSerializer(serializers.ModelSerializer):
    new_password = None
    phone_number = PhoneNumberField()
    invite_code = serializers.CharField(max_length=6, read_only=True)

    class Meta:
        model = User
        fields = ('phone_number', 'invite_code')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        if self.new_password is not None:
            rep['password'] = self.new_password
        rep['invite_users'] = UserSerializer(instance.children.all(), many=True).data
        return rep

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        password = user.create_password()
        self.new_password = password
        time.sleep(3)
        user.set_password(password)
        user.create_invite_code()
        user.save()
        return user


class AddAnotherUserSerializer(serializers.Serializer):
    invite_code = serializers.CharField(max_length=6)

    def validate_invite_code(self, invite_code):
        if not User.objects.filter(invite_code=invite_code).exists():
            raise serializers.ValidationError('Нет пользователя с таким invite code')
        return invite_code

    def create(self, validated_data):
        user = self.context.get('request').user
        user_with_invite_code = User.objects.get(**validated_data)
        user.parent = user_with_invite_code
        user.save()
        return user
