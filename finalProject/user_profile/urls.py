from django.urls import path
from .views import UserRegistrationView, UserDetailView, UserEditView, UserDeleteView, UserLoginView, UserLogoutView


urlpatterns = [
    path('create/', UserRegistrationView.as_view(), name='profile-create'),
    path('<int:pk>/details/', UserDetailView.as_view(), name='profile-details'),
    path('<int:pk>/edit/', UserEditView.as_view(), name='profile-edit'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='profile-delete'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]