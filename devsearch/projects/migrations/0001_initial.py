# Generated by Django 5.2.3 on 2025-06-30 09:33

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('descripiton', models.TextField(blank=True, null=True)),
                ('demo_link', models.CharField(
                    blank=True, max_length=2000, null=True)),
                ('source_code', models.CharField(
                    blank=True, max_length=2000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False,
                 primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
