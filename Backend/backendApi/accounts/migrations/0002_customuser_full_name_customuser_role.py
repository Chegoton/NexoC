# Generated by Django 5.0.3 on 2024-04-02 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='full_name',
            field=models.CharField(default='hola', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.IntegerField(choices=[(1, 'Admin'), (2, 'Usuario')], default=1),
            preserve_default=False,
        ),
    ]
