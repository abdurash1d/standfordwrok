# Generated by Django 5.1.3 on 2025-01-17 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_uploadedfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='extracted_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
