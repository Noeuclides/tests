# Generated by Django 2.2.8 on 2019-12-12 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user_task',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
