# Generated by Django 4.0.2 on 2022-02-27 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('image', models.CharField(default='https://picsum.photos/1000/1000', max_length=200)),
                ('postedAt', models.DateField(auto_now_add=True)),
                ('description', models.TextField()),
                ('tags', models.JSONField()),
            ],
        ),
    ]
