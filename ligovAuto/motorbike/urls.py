from django.urls import path
from .views import motorbike_create, MotorbikeDetailsView, MotorbikeEditView, MotorbikeDeleteView

urlpatterns = [
    path('create/', motorbike_create, name='motorbike-create'),
    path('<int:pk>/details/', MotorbikeDetailsView.as_view(), name='motorbike-details'),
    path('<int:pk>/edit/', MotorbikeEditView.as_view(), name='motorbike-edit'),
    path('<int:pk>/delete/', MotorbikeDeleteView.as_view(), name='motorbike-delete'),

]
