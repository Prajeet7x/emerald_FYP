# Generated by Django 3.2.7 on 2022-03-12 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emeraldApp', '0018_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='name',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
