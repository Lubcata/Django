# Generated by Django 5.0.6 on 2024-06-26 17:54

from django.db import migrations
from django.utils import timezone


def set_status(apps, schema_editor):
    order_model = apps.get_model('main_app', 'Order')

    for order in order_model.objects.all():
        if order.status == 'Pending':
            order.delivery = order.order_date + timezone.timedelta(days=3)
            order.save()
        elif order.status == 'Completed':
            order.warranty = '24 months'
            order.save()
        elif order.status == 'Cancelled':
            order.delete()


def reverse_delivery_and_warranty(apps, schema_editor):
    order_model = apps.get_model('main_app', 'Order')

    for order in order_model.objects.all():
        if order.status == "Pending":
            order.delivery = None
        elif order.status == "Completed":
            order.warranty = order_model._meta.get_field('warranty').default

        order.save()


class Migration(migrations.Migration):
    dependencies = [
        ('main_app', '0015_order'),
    ]

    operations = [
        migrations.RunPython(set_status, reverse_delivery_and_warranty)
    ]
