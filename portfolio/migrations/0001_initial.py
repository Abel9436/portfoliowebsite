# Generated by Django 5.0.1 on 2024-03-06 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=50)),
                ('project_description', models.TextField()),
                ('project_image', models.ImageField(upload_to=None)),
            ],
            options={
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Skill_name', models.CharField(max_length=50)),
                ('skill_level', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Skills',
            },
        ),
    ]
