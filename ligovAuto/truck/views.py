from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import modelform_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView

from .forms import TruckForm, TruckDeleteForm
from .models import Truck


# Create your views here.
@login_required
def truck_create(request):
    form = TruckForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        truck = form.save(commit=False)
        truck.user = request.user
        truck.save()
        return redirect('catalogue-trucks')
    return render(request, 'truck/truck-create.html', {'form': form})


class TruckDetailsView(DetailView):
    model = Truck
    template_name = 'truck/truck-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'owner': self.object.user
        })
        return context


class TruckEditView(LoginRequiredMixin, UpdateView):
    model = Truck
    template_name = 'truck/truck-edit.html'
    form_class = TruckForm

    def get_success_url(self):
        return reverse_lazy('truck-details', kwargs={'pk': self.object.pk})


class TruckDeleteView(LoginRequiredMixin, DeleteView):
    model = Truck
    template_name = 'truck/truck_delete.html'
    success_url = reverse_lazy('catalogue-trucks')
    form_class = modelform_factory(
        model=Truck,
        form=TruckDeleteForm,
        fields='__all__'
    )

    def get_form_kwargs(self):
        instance = self.get_object()
        form_kwargs = super().get_form_kwargs()

        form_kwargs.update(instance=instance)
        return form_kwargs
