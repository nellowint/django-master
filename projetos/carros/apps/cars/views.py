
from django.views.generic import (
    CreateView, 
    DeleteView,
    DetailView,
    ListView, 
    UpdateView, 
)
from .models import Car
from .forms import CarForm

class ListViewCar(ListView):
    model = Car
    template_name = 'cars/list.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().filter(is_active=True)
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(name__icontains=search)
        return cars

class CreateViewCar(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'cars/new.html'
    success_url = '/'

class DetailViewCar(DetailView):
    model = Car
    template_name = 'cars/detail.html'

class UpdateViewCar(UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'cars/update.html'
    success_url = '/'

class DeleteViewCar(DeleteView):
    pass