from django.shortcuts import render, redirect
from .forms import CarForm, CarDeleteForm
from .models import Car


# Create your views here.
def car_create(request):
    form = CarForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogue')
    return render(request, 'car/car-create.html', {'form': form})


def car_details(request, pk):
    car = Car.objects.get(pk=pk)
    return render(request, 'car/car-details.html', {'car': car})


def car_edit(request, pk):
    car = Car.objects.get(pk=pk)
    form = CarForm(request.POST or None, instance=car)
    if form.is_valid():
        form.save()
        return redirect('catalogue')
    context = {
        'car': car,
        'form': form
    }
    return render(request, 'car/car-edit.html', context=context)


def car_delete(request, pk):
    car = Car.objects.get(pk=pk)
    form = CarDeleteForm(request.POST or None, instance=car)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'form': form,
        'car': car
    }
    return render(request, 'car/car-delete.html', context)