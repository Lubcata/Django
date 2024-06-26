# Generated by Django 5.0.6 on 2024-06-25 07:06

from django.db import migrations


def create_unique_brands(apps, schema_editor):
    shoe = apps.get_model('main_app', 'Shoe')
    unique_brands = apps.get_model('main_app', 'UniqueBrands')

    unique_brand_name = shoe.objects.values_list('brand', flat=True).distinct()
    unique_brands.objects.bulk_create([unique_brands(brand=brand_name) for brand_name in unique_brand_name])


def reverse_unique_brand(apps, schema_editor):
    unique_brands = apps.get_model('main_app', 'UniqueBrands')
    unique_brands.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('main_app', '0002_uniquebrands'),
    ]

    operations = [
        migrations.RunPython(create_unique_brands, reverse_unique_brand)
    ]
