# Generated by Django 4.0.2 on 2022-02-28 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='tags',
            field=models.JSONField(default=[{'link': 'link goes here', 'message': 'link message'}]),
        ),
    ]