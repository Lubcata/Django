import os
from datetime import date, timedelta

import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()
# Import your models here

from main_app.models import Author, Book, Artist, Song, Product, Review, DrivingLicense, Driver, Owner, Car, \
    Registration


# Create queries within functions


def show_all_authors_with_their_books():
    books_with_authors = []

    authors = Author.objects.all().order_by('id')

    for author in authors:
        books = author.book_set.all()

        if not books:
            continue
        titles = ", ".join(b.title for b in books)

        books_with_authors.append(
            f"{author.name} has written - {titles}!"
        )

    return "\n".join(books_with_authors)


def delete_all_authors_without_books():
    authors_to_delete = Author.objects.filter(book__isnull=True).delete()


def add_song_to_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.add(song)


def get_songs_by_artist(artist_name: str):
    return Artist.objects.get(name=artist_name).songs.all().order_by('-id')


def remove_song_from_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.remove(song)


def calculate_average_rating_for_product_by_name(product_name: str):
    product = Product.objects.get(name=product_name)
    reviews = product.reviews.all()

    total_sum = sum(r.rating for r in reviews)
    avg_sum = total_sum / len(reviews)

    return avg_sum


def get_reviews_with_high_ratings(threshold: int):
    return Review.objects.filter(rating__gte=threshold)


def get_products_with_no_reviews():
    return Product.objects.filter(reviews__isnull=True).order_by('-name')


def delete_products_without_reviews():
    get_products_with_no_reviews().delete()


def calculate_licenses_expiration_dates():
    licenses = DrivingLicense.objects.order_by('-license_number')

    return "\n".join(str(l) for l in licenses)


def get_drivers_with_expired_licenses(due_date: date):
    expiration_date_cutoff = due_date - timedelta(days=365)

    drivers_with_expired_license = Driver.objects.filter(license__issue_date__gt=expiration_date_cutoff)

    return drivers_with_expired_license


def register_car_by_owner(owner: Owner):
    registration = Registration.objects.filter(car__isnull=True).first()
    car = Car.objects.filter(registration__isnull=True).first()

    car.owner = owner

    car.save()

    registration.registration_date = date.today()
    registration.car = car

    registration.save()

    return f"Successfully registered {car.model} to {owner.name} with registration number {registration.registration_number}."

