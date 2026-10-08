
from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.list_car, name='list_car'),
    path('new', views.new_car, name='new_car'),
    path('edit', views.edit_car, name='edit_car'),
]