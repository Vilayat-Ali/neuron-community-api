# Generated by Django 4.0.2 on 2022-02-28 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community_new',
            name='links',
            field=models.JSONField(),
        ),
    ]
