from django.urls import path
from .views import truck_create, TruckDetailsView, TruckEditView, TruckDeleteView

urlpatterns = [
    path('create/', truck_create, name='truck-create'),
    path('<int:pk>/details/', TruckDetailsView.as_view(), name='truck-details'),
    path('<int:pk>/edit/', TruckEditView.as_view(), name='truck-edit'),
    path('<int:pk>/delete/', TruckDeleteView.as_view(), name='truck-delete'),
]