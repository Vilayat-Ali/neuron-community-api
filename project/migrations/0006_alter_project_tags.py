# Generated by Django 4.0.2 on 2022-02-28 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_alter_project_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='tags',
            field=models.JSONField(default=[{'tagName': 'name of tag', 'tagType': 'tech, doc, web-app, package'}]),
        ),
    ]
