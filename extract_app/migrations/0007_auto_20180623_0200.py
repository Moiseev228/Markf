# Generated by Django 2.0.5 on 2018-06-22 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extract_app', '0006_auto_20180616_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='recepts',
            name='Exemption',
            field=models.CharField(default='Не льготный', max_length=20),
        ),
        migrations.AddField(
            model_name='recepts',
            name='Type_exemption',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]
