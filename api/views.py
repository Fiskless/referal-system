from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
from .models import CustomUser
from .serializers import CustomUserSerializer, CustomUserProfileSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from django.http import JsonResponse


class UserAuthorizationView(generics.CreateAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

    class Meta:
        model = CustomUser
        fields = ['phone', 'invite_code']


# @api_view(['GET'])
# @permission_classes((permissions.AllowAny,))
# def get_user_profile(request, pk):
#     user = CustomUser.objects.get(pk=pk)
#     print(user)
#     # invited_users = CustomUser.objects.filter(
#     #     another_invite_code=user.invite_code)
#     # content = {}
#     # content["Информация о пользователе"] = user
#     # if not invited_users:
#     #     content['Приглашенные пользователи'] = 'Нет приглашенных пользователей'
#     # else:
#     #     content['Приглашенные пользователи'] = invited_users
#     return Response(user)


class UserView(generics.RetrieveAPIView):

    serializer_class = CustomUserProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self):
        user = CustomUser.objects.get(pk=self.kwargs['pk'])
        return user


# class UserView(APIView):
#
#     serializer_class = CustomUserProfileSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#     def get(self, request, format=None):
#         user = CustomUser.objects.get(pk=self.kwargs['pk'])
#         invited_users = CustomUser.objects.filter(another_invite_code=user.invite_code)
#         content = {}
#         content["Информация о пользователе"] = user
#         if not invited_users:
#             content['Приглашенные пользователи'] = 'Нет приглашенных пользователей'
#         else:
#             content['Приглашенные пользователи'] = invited_users
#         return Response(content)