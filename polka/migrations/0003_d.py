# Generated by Django 4.2.9 on 2024-01-22 17:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('polka', '0002_publisher_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='D',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
            ],
        ),
    ]