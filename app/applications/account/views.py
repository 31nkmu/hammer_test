from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from applications.account import serializers

User = get_user_model()


class RegisterApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.RegisterSerializer

    @swagger_auto_schema(tags=['account'], request_body=serializers.RegisterSerializer)
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class FullRegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.FullRegisterSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(tags=['account'], request_body=serializers.FullRegisterSerializer)
    def post(self, request):
        return super().post(request)


class ActivationApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.ActivateSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(tags=['account'], request_body=serializers.ActivateSerializer)
    def post(self, request):
        code = request.data['code']
        user = request.user
        if user.activation_code == code:
            user.full_registered = True
            user.activation_code = ''
            user.save(update_fields=['activation_code', 'full_registered'])
            return Response({'msg': 'Вы успешно прошли регистрацию'}, status=status.HTTP_200_OK)
        else:
            return Response({'msg': 'Неверный код'})


class ChangePasswordApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.ChangePasswordSerializer
    permission_classes = [IsAuthenticated]


class ForgotPasswordApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.ForgotPasswordSerializer


class ForgotPasswordConfirmApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.ForgotPasswordConfirmSerializer


class ForgotPasswordCodewordApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.ForgotPasswordCodewordSerializer


# class ForgotPasswordPhoneApiView(CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = serializers.ForgotPasswordPhoneSerializer
#


