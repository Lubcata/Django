# Generated by Django 5.0.4 on 2024-06-30 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_artifact'),
    ]

    operations = [
        migrations.AddField(
            model_name='artifact',
            name='age',
            field=models.PositiveIntegerField(default=100),
            preserve_default=False,
        ),
    ]
