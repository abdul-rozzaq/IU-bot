# Generated by Django 4.2.5 on 2023-09-14 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='telegram_id',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=128, null=True),
        ),
    ]