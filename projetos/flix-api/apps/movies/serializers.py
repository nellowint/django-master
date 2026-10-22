
from django.db.models import Avg
from rest_framework import serializers

from apps.actors.serializers import ActorSerializer
from apps.genres.serializers import GenreSerializer

from .models import Movie


class MovieSerializer(serializers.ModelSerializer):

    actors = ActorSerializer(many=True)
    genre = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta():
        model = Movie
        fields = [
            'id',
            'rate',
            'title',
            'sinopse',
            'genre',
            'actors',
            'release_date',
        ]

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        if rate:
            return round(rate, 1)
        return 'Sem Avaliação'


class MovieModelSerializer(serializers.ModelSerializer):

    class Meta():
        model = Movie
        fields = '__all__'

    def validate_sinopse(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('Máximo de 500 caracteres')
        return value
