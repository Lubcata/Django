# Generated by Django 5.0.4 on 2024-06-26 17:16

from django.db import migrations


def set_price(apps, schema_editor):
    MULTIPLIER = 120

    phone_model = apps.get_model('main_app', 'Smartphone')
    phones = phone_model.objects.all()

    for phone in phones:
        phone.price = MULTIPLIER * len(phone.brand)

        phone.save()


def set_category(apps, schema_editor):
    phone_model = apps.get_model('main_app', 'Smartphone')

    for phone in phone_model.objects.all():
        if phone.price >= 750:
            phone.category = 'Expensive'
        else:
            phone.category = 'Cheap'

        phone.save()


def set_price_category_to_default(apps, schema_editor):
    phone_model = apps.get_model('main_app', 'Smartphone')
    phones = phone_model.objects.all()

    for phone in phones:
        phone.price = phone_model._meta.get_field('price').default
        phone.category = phone_model._meta.get_field('category').default

        phone.save()


def set_all_colums(apps, schema_editor):
    set_price(apps, schema_editor)
    set_category(apps, schema_editor)


class Migration(migrations.Migration):
    dependencies = [
        ('main_app', '0013_smartphone'),
    ]

    operations = [
        migrations.RunPython(set_all_colums, set_price_category_to_default)
    ]
