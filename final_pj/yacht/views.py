from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import modelform_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView

from .forms import YachtForm, YachtDeleteForm
from .models import Yacht


# Create your views here.
@login_required
def yacht_create(request):
    form = YachtForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        yacht = form.save(commit=False)
        yacht.user = request.user
        yacht.save()
        return redirect('catalogue-yachts')
    return render(request, 'yacht/yacht-create.html', {'form': form})


class YachtDetailsView(DetailView):
    model = Yacht
    template_name = 'yacht/yacht-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'owner': self.object.user
        })
        return context


class YachtEditView(LoginRequiredMixin, UpdateView):
    model = Yacht
    template_name = 'yacht/yacht-edit.html'
    form_class = YachtForm

    def get_success_url(self):
        return reverse_lazy('yacht-details', kwargs={'pk': self.object.pk})


class YachtDeleteView(LoginRequiredMixin, DeleteView):
    model = Yacht
    template_name = 'yacht/yacht-delete.html'
    success_url = reverse_lazy('catalogue-yachts')
    form_class = modelform_factory(
        model=Yacht,
        form=YachtDeleteForm,
        fields='__all__'
    )

    def get_form_kwargs(self):
        instance = self.get_object()
        form_kwargs = super().get_form_kwargs()

        form_kwargs.update(instance=instance)
        return form_kwargs
