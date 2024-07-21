# Generated by Django 5.0.4 on 2024-07-21 14:05

import main_app.mixins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_product_alter_book_author_alter_book_isbn_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('hero_title', models.CharField(max_length=100)),
                ('energy', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FlashHero',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('main_app.hero',),
        ),
        migrations.CreateModel(
            name='SpiderHero',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('main_app.hero', main_app.mixins.RechargeEnergyMixin),
        ),
    ]
