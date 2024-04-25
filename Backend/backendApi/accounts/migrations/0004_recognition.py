# Generated by Django 5.0.3 on 2024-04-23 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_satisfactionsurvey'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recognition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selected_employee', models.CharField(blank=True, max_length=100)),
                ('selected_recognition', models.CharField(blank=True, max_length=100)),
                ('recognition_message', models.TextField(blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
