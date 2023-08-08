import time

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from applications.account import serializers

User = get_user_model()


class AuthApiView(CreateAPIView, ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.AuthSerializer

    def perform_create(self, serializer):
        phone_number = serializer.validated_data['phone_number']

        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            user = None

        if user:
            new_password = user.create_password()
            user.set_password(new_password)
            user.save()
            return Response({
                'phone_number': str(phone_number),
                'password': new_password,
                'invite_code': user.invite_code,
            }, status=status.HTTP_201_CREATED)
        else:
            serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_response = self.perform_create(serializer)
        if updated_response:
            time.sleep(3)
            return updated_response
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserDetailAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.AuthSerializer


class AddAnotherUserAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.AddAnotherUserSerializer
    permission_classes = (IsAuthenticated,)
