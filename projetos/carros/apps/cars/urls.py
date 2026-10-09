
from django.urls import path
from .views import (
    CreateViewCar, 
    DeleteViewCar,
    DetailViewCar,
    ListViewCar, 
    UpdateViewCar, 
)

app_name = 'cars'

urlpatterns = [
    path('', ListViewCar.as_view(), name='list_car'),
    path('new', CreateViewCar.as_view(), name='new_car'),
    path('detail/<int:pk>/', DetailViewCar.as_view(), name='detail_car'),
    path('update/<int:pk>/', UpdateViewCar.as_view(), name='update_car'),
    path('delete/<int:pk>/', DeleteViewCar.as_view(), name='delete_car'),
]