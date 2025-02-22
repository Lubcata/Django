# Generated by Django 5.0.6 on 2024-06-21 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('code', models.CharField(max_length=4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('employees_count', models.PositiveIntegerField(default=1)),
                ('location', models.CharField(choices=[('Sf', 'Sofia'), ('Pv', 'Plovdiv'), ('Br', 'Burgas'), ('Vr', 'Varna')], max_length=20)),
                ('last_edited_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
