
from django.db.models import Avg
from rest_framework import serializers

from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(
        read_only=True
    )

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        if rate:
            return round(rate, 1)
        return 'Sem Avaliação'

    def validate_sinopse(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('Máximo de 500 caracteres')
        return value

    class Meta():
        model = Movie
        fields = '__all__'
