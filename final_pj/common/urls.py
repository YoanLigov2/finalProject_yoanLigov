from django.urls import path
from .views import index, catalogue, add_vehicle, CatalogueMotorbikes, CatalogueCars, CatalogueYachts, CatalogueTrucks


urlpatterns = [
    path('', index, name='index'),
    path('pre-catalogue/', catalogue, name='catalogue'),
    path('add-vehicle/', add_vehicle, name='add-vehicle'),
    path('catalogue-cars/', CatalogueCars.as_view(), name='catalogue-cars'),
    path('catalogue-trucks/', CatalogueTrucks.as_view(), name='catalogue-trucks'),
    path('catalogue-yachts/', CatalogueYachts.as_view(), name='catalogue-yachts'),
    path('catalogue-motorbikes/', CatalogueMotorbikes.as_view(), name='catalogue-motorbikes'),
]
