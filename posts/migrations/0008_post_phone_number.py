# Generated by Django 3.2.16 on 2023-01-17 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_multipleimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='phone_number',
            field=models.CharField(default='0', max_length=200),
        ),
    ]
