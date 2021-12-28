from django.contrib import admin
from film_library.models import Cinema, Movie, Review, Genre

admin.site.register(Cinema)
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Genre)