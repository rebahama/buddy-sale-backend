# Generated by Django 3.2.16 on 2023-01-17 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_post_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='email',
            field=models.CharField(default='', max_length=500),
        ),
    ]
