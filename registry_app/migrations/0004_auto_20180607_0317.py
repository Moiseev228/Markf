# Generated by Django 2.0.5 on 2018-06-07 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry_app', '0003_auto_20180604_0445'),
    ]

    operations = [
        migrations.AddField(
            model_name='patiens',
            name='date_of_birth',
            field=models.CharField(default=' ', max_length=8),
        ),
        migrations.AddField(
            model_name='patiens',
            name='phone',
            field=models.CharField(default=' ', max_length=11),
        ),
        migrations.AddField(
            model_name='patiens',
            name='sector',
            field=models.CharField(default=' ', max_length=30),
        ),
    ]
