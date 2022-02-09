# Generated by Django 3.2.8 on 2022-01-07 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Islington Web Development Club', 'Islington Web Development Club'), ('Islington AI Club', 'Islington AI Club'), ('Cyber Defenders Club', 'Cyber Defenders Club'), ('Cyber Ops Club', 'Cyber Ops Club'), ('Multimedia Club', 'Multimedia Club')], max_length=50, null=True)),
                ('faculty', models.CharField(max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('faculty', models.CharField(max_length=50, null=True)),
                ('timing', models.CharField(max_length=30, null=True)),
                ('venue', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('collegeEmail', models.CharField(max_length=50, null=True)),
                ('personalEmail', models.CharField(max_length=50, null=True)),
                ('year', models.CharField(choices=[('Year 1', 'Year 1'), ('Year 2', 'Year 2'), ('Year 3', 'Year 3'), ('Graduated', 'Graduated')], max_length=10, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='President',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('collegeEmail', models.CharField(max_length=50, null=True)),
                ('personalEmail', models.CharField(max_length=50, null=True)),
                ('year', models.CharField(choices=[('Year 1', 'Year 1'), ('Year 2', 'Year 2'), ('Year 3', 'Year 3'), ('Graduated', 'Graduated')], max_length=10, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]