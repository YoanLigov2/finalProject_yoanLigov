from django.urls import reverse_lazy

from .forms import CollectionUserCreationForm, LoginForm, CollectionUserEditForm
from .models import CollectionUser
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


class UserRegistrationView(CreateView):
    model = CollectionUser
    form_class = CollectionUserCreationForm
    template_name = 'profile/profile-create.html'
    success_url = reverse_lazy('login')


class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'profile/login.html'
    next_page = reverse_lazy('index')


class UserLogoutView(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('login')


class UserDetailView(LoginRequiredMixin, DetailView):
    model = CollectionUser
    template_name = 'profile/profile-details.html'


class UserEditView(LoginRequiredMixin, UpdateView):
    model = CollectionUser
    form_class = CollectionUserEditForm
    template_name = 'profile/profile-edit.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = CollectionUser
    template_name = 'profile/profile-delete.html'
    success_url = reverse_lazy('index')




