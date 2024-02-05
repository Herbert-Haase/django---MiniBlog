# Generated by Django 5.0.1 on 2024-02-05 17:38

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular comment across blogs', primary_key=True, serialize=False),
        ),
    ]