# Generated by Django 5.0.1 on 2024-03-08 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_project_project_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientMassage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=50)),
                ('sender_email', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=70)),
            ],
        ),
    ]