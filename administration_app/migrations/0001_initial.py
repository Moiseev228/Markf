# Generated by Django 2.0.5 on 2018-05-15 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=124)),
                ('adress', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=16)),
                ('post', models.CharField(max_length=100)),
                ('specialization', models.CharField(max_length=100)),
                ('passport', models.CharField(max_length=11)),
            ],
        ),
    ]
