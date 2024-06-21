from datetime import date

from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=30)
    email_address = models.EmailField()
    photo = models.URLField()
    birth_date = models.DateField()
    works_full_time = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)


class DepartmentChoices(models.TextChoices):
    SOFIA = "Sf", "Sofia"
    PLOVDIV = "Pv", "Plovdiv"
    BURGAS = "Br", "Burgas"
    VARNA = "Vr", "Varna"


class Department(models.Model):
    code = models.CharField(max_length=4, primary_key=True, unique=True)
    name = models.CharField(max_length=50, unique=True)
    employees_count = models.PositiveIntegerField(default=1)
    location = models.CharField(max_length=20, choices=DepartmentChoices.choices)
    last_edited_on = models.DateTimeField(auto_now=True, editable=False)


class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    duration_in_days = models.PositiveIntegerField(verbose_name="Duration in Days")
    estimated_hours = models.FloatField(verbose_name="Estimated Hours")
    start_date = models.DateField(default=date.today, verbose_name="Start Date")
    created_on = models.DateField(auto_now_add=True, editable=False)
    last_edited_on = models.DateField(auto_now=True, editable=False)

