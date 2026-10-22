
from django.db.models import Avg, Count
from rest_framework import generics, response, status, views
from rest_framework.permissions import IsAuthenticated

from apps.reviews.models import Review
from core.permissions import CustomPermissions

from .models import Movie
from .serializers import MovieSerializer


class MovieListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, CustomPermissions,)
    queryset = Movie.objects.filter(is_active=True)
    serializer_class = MovieSerializer


class MovieRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, CustomPermissions,)
    queryset = Movie.objects.filter(is_active=True)
    serializer_class = MovieSerializer


class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, CustomPermissions,)
    queryset = Movie.objects.filter(is_active=True)

    def get(self, request):
        total_movies = self.queryset.count()
        movies_by_genre = (self.queryset.values('genre__name')
                           .annotate(count=Count('id')))
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(
            avg_stars=Avg('stars'))['avg_stars']

        movies_stats = {
            'total_movies': total_movies,
            'movies_by_genre': movies_by_genre,
            'total_reviews': total_reviews,
            'average_stars': round(average_stars, 1) if average_stars else 0,
        }

        return response.Response(
            data=movies_stats,
            status=status.HTTP_200_OK,
        )
