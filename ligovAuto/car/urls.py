from django.urls import path
from .views import car_create, CarDetailsView, CarEditView, CarDeleteView


urlpatterns = [
    path('create/', car_create, name='car-create'),
    path('<int:pk>/details/', CarDetailsView.as_view(), name='car-details'),
    path('<int:pk>/edit/', CarEditView.as_view(), name='car-edit'),
    path('<int:pk>/delete/', CarDeleteView.as_view(), name='car-delete'),
]