
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView, 
    SpectacularRedocView,
    SpectacularSwaggerView
)  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/v1/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/v1/auths/', include('apps.auths.urls')),
    path('api/v1/genres/', include('apps.genres.urls')),
    path('api/v1/actors/', include('apps.actors.urls')),
    path('api/v1/movies/', include('apps.movies.urls')),
    path('api/v1/reviews/', include('apps.reviews.urls')),
]