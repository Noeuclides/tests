# Generated by Django 2.2.8 on 2019-12-12 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20191212_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='state',
            field=models.CharField(choices=[(True, 'Done.'), (False, 'To Do.')], default=False, max_length=8),
        ),
    ]
