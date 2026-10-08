
from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm


def list_car(request):
    search = request.GET.get('search')
    if search:
        cars = Car.objects.filter(name__icontains=search, is_active=True)
    else:
        cars = Car.objects.filter(is_active=True)
    return render(request, 'cars/list.html', {'cars': cars})

def new_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_car')
    else:
        form = CarForm()
    return render(request, 'cars/new.html', { 'form': form })

def edit_car(request, pk):
    pass