# Generated by Django 2.0.5 on 2018-05-18 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administration_app', '0005_remove_staff_login_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='name_employee',
        ),
    ]
