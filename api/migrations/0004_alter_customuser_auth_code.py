# Generated by Django 4.0.3 on 2022-03-27 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_customuser_auth_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='auth_code',
            field=models.IntegerField(default=3451, unique=True, verbose_name='Код для авторизации'),
        ),
    ]
