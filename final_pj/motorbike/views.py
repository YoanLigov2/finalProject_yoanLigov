from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import modelform_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView

from .forms import MotorbikeForm, MotorbikeDeleteForm
from .models import Motorbike


# Create your views here.
@login_required
def motorbike_create(request):
    form = MotorbikeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        bike = form.save(commit=False)
        bike.user = request.user
        bike.save()
        return redirect('catalogue-motorbikes')
    return render(request, 'motorbike/motorbike-create.html', {'form': form})


class MotorbikeDetailsView(DetailView):
    model = Motorbike
    template_name = 'motorbike/motorbike-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'owner': self.object.user
        })
        return context


class MotorbikeEditView(LoginRequiredMixin, UpdateView):
    model = Motorbike
    template_name = 'motorbike/motorbike-edit.html'
    form_class = MotorbikeForm

    def get_success_url(self):
        return reverse_lazy('motorbike-details', kwargs={'pk': self.object.pk})


class MotorbikeDeleteView(LoginRequiredMixin, DeleteView):
    model = Motorbike
    template_name = 'motorbike/motorbike-delete.html'
    success_url = reverse_lazy('catalogue-motorbikes')
    form_class = modelform_factory(
        model=Motorbike,
        form=MotorbikeDeleteForm,
        fields='__all__'
    )

    def get_form_kwargs(self):
        instance = self.get_object()
        form_kwargs = super().get_form_kwargs()

        form_kwargs.update(instance=instance)
        return form_kwargs
