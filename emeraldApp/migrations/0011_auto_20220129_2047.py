# Generated by Django 3.2.7 on 2022-01-29 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emeraldApp', '0010_alter_member_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='specialisation',
            field=models.CharField(choices=[('Computing', 'Computing'), ('Networking', 'Networking'), ('Multimedia', 'Multimedia')], max_length=20, null=True),
        ),
    ]
