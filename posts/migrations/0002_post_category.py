# Generated by Django 3.2.16 on 2022-12-15 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='category.category'),
        ),
    ]
