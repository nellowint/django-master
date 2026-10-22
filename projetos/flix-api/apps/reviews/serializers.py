
from rest_framework import serializers

from apps.movies.serializers import MovieSerializer

from .models import Review


class ReviewSerializer(serializers.ModelSerializer):

    movie = MovieSerializer()

    class Meta():
        model = Review
        fields = [
            'id',
            'stars',
            'comment',
            'movie',
        ]


class ReviewModelSerializer(serializers.ModelSerializer):

    class Meta():
        model = Review
        fields = '__all__'
