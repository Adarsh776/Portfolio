# Generated by Django 5.2 on 2025-04-11 17:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('profile_image', models.ImageField(upload_to='profile_images/')),
                ('resume', models.FileField(blank=True, null=True, upload_to='resumes/')),
                ('social_links', models.JSONField(default=dict)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='projects/')),
                ('github_link', models.URLField(blank=True, null=True)),
                ('live_demo_link', models.URLField(blank=True, null=True)),
                ('tech_stack', models.CharField(max_length=200)),
                ('is_featured', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SkillModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=100)),
                ('skill_level', models.IntegerField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='app.profilemodel')),
            ],
        ),
    ]
