from django.contrib import admin
from django.urls import path
from film_library import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/movie/", views.movie_list_view),
    path("api/v1/movie/<int:id>", views.movie_detail_view),
]
