
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .forms import CarForm
from .models import Car


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


class DetailViewCar(DetailView):
    model = Car
    template_name = 'cars/detail.html'


@method_decorator(login_required(
    login_url='accounts:login_view'), name='dispatch'
)
class CreateViewCar(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'cars/new.html'
    success_url = '/cars/'


@method_decorator(login_required(
    login_url='accounts:login_view'), name='dispatch'
)
class UpdateViewCar(UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'cars/update.html'

    def get_success_url(self):
        return reverse_lazy('cars:detail_car', kwargs={'pk': self.object.pk})


@method_decorator(login_required(
    login_url='accounts:login_view'), name='dispatch'
)
class DeleteViewCar(DeleteView):
    model = Car
    template_name = 'cars/delete.html'
    success_url = '/cars/'
