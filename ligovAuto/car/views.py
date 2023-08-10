from django.contrib.auth.decorators import login_required
from django.forms import modelform_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CarForm, CarDeleteForm
from .models import Car


# Create your views here.
@login_required
def car_create(request):
    form = CarForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        car = form.save(commit=False)
        car.user = request.user
        car.save()
        return redirect('catalogue-cars')
    return render(request, 'car/car-create.html', {'form': form})


class CarDetailsView(DetailView):
    model = Car
    template_name = 'car/car-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'owner': self.object.user
        })
        return context


class CarEditView(LoginRequiredMixin, UpdateView):
    model = Car
    template_name = 'car/car-edit.html'
    form_class = CarForm

    def get_success_url(self):
        return reverse_lazy('car-details', kwargs={'pk': self.object.pk})


class CarDeleteView(LoginRequiredMixin, DeleteView):
    model = Car
    template_name = 'car/car-delete.html'
    success_url = reverse_lazy('catalogue')
    form_class = modelform_factory(
        model=Car,
        form=CarDeleteForm,
        fields='__all__'
    )

    def get_form_kwargs(self):
        instance = self.get_object()
        form_kwargs = super().get_form_kwargs()

        form_kwargs.update(instance=instance)
        return form_kwargs
