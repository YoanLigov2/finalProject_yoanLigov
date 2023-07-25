from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView

from finalProject.car.models import Car
from finalProject.truck.models import Truck
from finalProject.motorbike.models import Motorbike
from finalProject.yacht.models import Yacht


# Create your views here.
def index(request):
    return render(request, 'common/index.html')


def catalogue(request):
    return render(request, 'catalogue_slash_add-vehicle/pre-catalogue.html')


@login_required
def add_vehicle(request):
    return render(request, 'catalogue_slash_add-vehicle/add-vehicle-page.html')


class CatalogueYachts(ListView):
    model = Yacht
    template_name = 'yacht/catalogue-yachts.html'


class CatalogueTrucks(ListView):
    model = Truck
    template_name = 'truck/catalogue-trucks.html'


class CatalogueMotorbikes(ListView):
    model = Motorbike
    template_name = 'motorbike/catalogue-motorbikes.html'


class CatalogueCars(ListView):
    model = Car
    template_name = 'car/catalogue.html'
