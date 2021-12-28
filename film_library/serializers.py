from rest_framework import serializers
from . import models

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = "title description cinema genre".split()
