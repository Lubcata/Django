import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet, Artifact, Location, Car, Task


# Create queries within functions
def create_pet(name: str, species: str):
    pet = Pet.objects.create(name=name, species=species)
    return f"{pet.name} is a very cute {pet.species}!"


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    artifact = Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical,
    )

    return f"The artifact {artifact.name} is {artifact.age} years old!"


def rename_artifact(artifact: Artifact, new_name: str):
    # Artifact.objects.filter(is_magical=True, age__gt=250, pk=Artifact.pk).update(name=new_name)

    if artifact.is_magical and artifact.age > 250:
        artifact.name = new_name
        artifact.save()


def delete_all_artifacts():
    Artifact.objects.all().delete()


def show_all_locations():
    locations = Location.objects.all().order_by('-id')

    return "\n".join(str(location) for location in locations)


def new_capital():
    location = Location.objects.first()
    location.is_capital = True
    location.save()


def get_capitals():
    return Location.objects.filter(is_capital=True).values('name')


def delete_first_location():
    Location.objects.filter().delete()


def apply_discount():
    cars = Car.objects.all()

    for car in cars:
        percent_of_discount = sum(int(digit) for digit in str(car.year)) / 100
        discount = float(car.price) * percent_of_discount
        car.price_with_discount = float(car.price) - discount
        car.save()


def get_recent_cars():
    return Car.objects.filter(year__gt=2000).values('model', 'price_with_discount')


def delete_last_car() -> None:
    Car.objects.last().delete()


def show_unfinished_tasks():
    tasks = Task.objects.filter(is_finished=False)

    return "\n".join(str(t) for t in tasks)


def complete_odd_tasks():
    tasks = Task.objects.all()

    for task in tasks:
        if task.id % 2 == 1:
            task.is_finished = True

    Task.objects.bulk.update(tasks, ['is_finished'])


def encode_and_replace(text: str, task_title: str):
    

