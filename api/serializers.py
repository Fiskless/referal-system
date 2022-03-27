from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import CustomUser, RelatedUsers
from django.utils.crypto import get_random_string


class AuthCodeSerializer(serializers.Serializer):
    auth_code = serializers.IntegerField()

    def validate(self, attrs):

        auth_code = attrs['auth_code']
        user = CustomUser.objects.filter(auth_code=auth_code)
        if not user:
            raise serializers.ValidationError(
                {auth_code: "Неправильный код авторизации"})
        return attrs


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser

        fields = [
            'phone',
            'another_invite_code',
        ]

    def create(self, validated_data):

        phone = self.validated_data['phone']
        code = self.validated_data.get('another_invite_code')
        inviter = CustomUser.objects.filter(
            invite_code=code
        ).first()
        if code and not inviter:
            raise serializers.ValidationError(
                {code: "Такого инвайт-кода не существует"})
        invite_code = get_random_string(length=6)
        existed_user = CustomUser.objects.filter(phone=phone)
        if not existed_user and code:
            user = CustomUser.objects.create(
                username=phone,
                phone=phone,
                invite_code=invite_code,
                another_invite_code=code,
            )
            RelatedUsers.objects.create(
                inviter=inviter,
                invited_by_user=user,
            )
        if not existed_user and not code:
            user = CustomUser.objects.create(
                username=phone,
                phone=phone,
                invite_code=invite_code,
            )
        else:
            user = existed_user.first()
        return user


class CustomUserProfileSerializer(serializers.ModelSerializer):
    users_invited = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = CustomUser

        fields = [
            'phone',
            'another_invite_code',
            'invite_code',
            'users_invited',
        ]


