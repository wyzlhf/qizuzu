# Generated by Django 3.2.6 on 2021-08-05 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0004_auto_20210805_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='company',
            field=models.CharField(max_length=200, verbose_name='用户公司'),
        ),
    ]