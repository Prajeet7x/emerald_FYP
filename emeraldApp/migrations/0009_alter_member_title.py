# Generated by Django 3.2.7 on 2022-01-29 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emeraldApp', '0008_member_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='title',
            field=models.CharField(choices=[('President', 'President'), ('Advisor', 'Advisor'), ('Vice President', 'Vice President'), ('Event Manager', 'Event Manager'), ('Treasurer', 'Treasurer'), ('Core Member', 'Core Member'), ('General Member', 'General Member')], max_length=40, null=True),
        ),
    ]
