from django.db import models



class Cinema(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Cinema, related_name="cinema_genres")


    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie

class Genre(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name



