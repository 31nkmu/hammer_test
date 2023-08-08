# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework_simplejwt.tokens import RefreshToken
#
#
# class CustomTokenObtainPairView(TokenObtainPairView):
#     def post(self, request, *args, **kwargs):
#         phone_number = request.data.get('username')
#         auth_code = request.data.get('password')
#
#         try:
#             client = User.objects.get(phone_number=phone_number, auth_code=auth_code)
#         except User.DoesNotExist:
#             return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
#
#         refresh = RefreshToken.for_user(client)
#         access_token = refresh.access_token
#
#         return Response({
#             'access': str(access_token),
#             'refresh': str(refresh),
#         })
#
#
# class CustomTokenRefreshView(TokenRefreshView):
#     def post(self, request, *args, **kwargs):
#         phone_number = request.data.get('username')
#         auth_code = request.data.get('password')
#
#         try:
#             client = User.objects.get(phone_number=phone_number, auth_code=auth_code)
#         except User.DoesNotExist:
#             return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
#
#         refresh = self.serializer_class.get_token(client)
#
#         return Response({
#             'refresh': str(refresh),
#         })
