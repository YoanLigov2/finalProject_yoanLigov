from django.urls import path
from .views import yacht_create, YachtDetailsView, YachtEditView, YachtDeleteView

urlpatterns = [
    path('create/', yacht_create, name='yacht-create'),
    path('<int:pk>/details/', YachtDetailsView.as_view(), name='yacht-details'),
    path('<int:pk>/edit/', YachtEditView.as_view(), name='yacht-edit'),
    path('<int:pk>/delete/', YachtDeleteView.as_view(), name='yacht-delete'),
]