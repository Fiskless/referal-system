from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
from .models import CustomUser
from .serializers import CustomUserSerializer, CustomUserProfileSerializer, AuthCodeSerializer

from django.contrib.auth import authenticate


class AuthCodeView(generics.CreateAPIView):

    serializer_class = AuthCodeSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        auth_code_ser = AuthCodeSerializer(data=request.data)
        auth_code_ser.is_valid(raise_exception=True)
        logged_in_user = CustomUser.objects.get(auth_code=auth_code_ser.data['auth_code'])
        authenticate(phone=logged_in_user.phone)
        resp = {'phone': str(logged_in_user.phone),
                'another_invite_code': logged_in_user.another_invite_code,
                'invite_code': logged_in_user.invite_code,
                'invited_users': logged_in_user.invited_users}
        return Response(resp)


class UserAuthorizationView(generics.CreateAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]


class UserView(generics.RetrieveAPIView):

    serializer_class = CustomUserProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self):
        user = CustomUser.objects.get(pk=self.kwargs['pk'])
        return user
