# Generated by Django 5.0.1 on 2024-01-25 15:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(default='static/images/default.png', upload_to='static/images')),
                ('parish_name', models.CharField(max_length=255)),
                ('parish_location', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AreaRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('week', models.CharField(choices=[('WEEK 1', 'WEEK 1'), ('WEEK 2', 'WEEK 2'), ('WEEK 3', 'WEEK 3'), ('WEEK 4', 'WEEK 4'), ('WEEK 5', 'WEEK 5')], max_length=7)),
                ('area_name', models.CharField(max_length=100)),
                ('parish_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('area_coordinator', models.CharField(max_length=100)),
                ('parish_number_with_report', models.PositiveIntegerField(default=0)),
                ('parish_number_with_no_report', models.PositiveIntegerField(default=0)),
                ('total_number_of_parish', models.PositiveIntegerField(default=0)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profile')),
            ],
        ),
    ]
