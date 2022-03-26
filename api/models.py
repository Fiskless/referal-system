from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    phone = PhoneNumberField('Мобильный телефон',
                             null=True,
                             help_text='Введите номер телефона, например, +79999999999')
    invite_code = models.CharField('Твой собственный инвайт-код',
                                   blank=True,
                                   max_length=6)
    another_invite_code = models.CharField('Введите чужой инвайт код, если он у вас есть',
                                   blank=True,
                                   max_length=6)
    invited_users = models.ForeignKey('self',
                                      blank=True,
                                      null=True,
                                      verbose_name='Приглашенные вами пользователи',
                                      on_delete=models.CASCADE)

    def __str__(self):
        return str(self.phone)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

#
# class RelatedUsers(models.Model):
#     inviter = models.ForeignKey(CustomUser,
#                                 blank=True,
#                                 null=True,
#                                 verbose_name='Пользователь, который пригласил',
#                                 on_delete=models.CASCADE)
#     invited_by_user = models.ForeignKey(CustomUser,
#                                         blank=True,
#                                         null=True,
#                                         verbose_name='Пользователь, которого пригласили',
#                                         on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.inviter
#
#     class Meta:
#         verbose_name = 'Связанный пользователь'
#         verbose_name_plural = 'Связанные пользователи'