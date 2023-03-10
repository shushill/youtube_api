# Generated by Django 3.2 on 2022-12-15 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VideoDetail',
            fields=[
                ('video_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('publishedAt', models.DateTimeField(max_length=50)),
                ('video_title', models.TextField(blank=True)),
                ('video_desc', models.TextField(blank=True)),
                ('thumbnail_url', models.TextField(blank=True)),
            ],
        ),
    ]
