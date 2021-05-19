from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework_jwt.views import JSONWebTokenAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from AuthAppApi.Serializers.UserSerializers import UserSerializer
from AuthAppApi.Serializers.loginSerializer import UserLoginSerializer
from AuthAppApi.models import Users



class UserSignupView(CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()


class UserUpdateView(UpdateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()


class UserDeleteView(DestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
