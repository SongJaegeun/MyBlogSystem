# Generated by Django 3.0.8 on 2020-08-07 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20, unique=True, verbose_name='아이디')),
                ('user_nm', models.CharField(max_length=10, verbose_name='이름')),
                ('user_pw', models.CharField(max_length=20, verbose_name='비밀번호')),
                ('email', models.EmailField(max_length=50, verbose_name='이메일')),
                ('reg_time', models.DateTimeField(auto_now_add=True, verbose_name='가입일')),
            ],
        ),
    ]
