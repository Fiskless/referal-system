from rest_framework import serializers
from .models import CustomUser
from django.utils.crypto import get_random_string


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
        are_users_related = False
        if code:
            invited_by_user = CustomUser.objects.filter(
                    invite_code=code
            ).first()
            if not invited_by_user:
                raise serializers.ValidationError(
                    {code: "Такого инвайт-кода не существует"})
            else:
                are_users_related = True

        invite_code = get_random_string(length=6)
        existed_user = CustomUser.objects.filter(phone=phone)
        if not existed_user:
            user = CustomUser.objects.create(
                username=phone,
                phone=phone,
                invite_code=invite_code,
                another_invite_code=code,
            )
        else:
            user = existed_user.first
        if are_users_related:
            invited_by_user.invited_users = user
            invited_by_user.save()
            print(invited_by_user.phone)
        return user


class CustomUserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser

        fields = [
            'phone',
            'another_invite_code',
            'invite_code',
            'invited_users',
        ]