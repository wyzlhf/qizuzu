# Generated by Django 3.2.6 on 2021-08-04 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号码')),
                ('verify_code', models.CharField(max_length=10, verbose_name='验证码')),
                ('is_actived', models.BooleanField(default=False, verbose_name='是否激活')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='最近登录时间')),
            ],
            options={
                'verbose_name': '用户数据',
                'verbose_name_plural': '用户数据',
                'ordering': ['-created'],
            },
        ),
    ]