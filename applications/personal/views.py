from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    View,
    UpdateView,
    DeleteView,
    ListView,
    TemplateView
)
from django.views.generic.edit import (
    FormView
)

from .models import Personal
from .forms import PersonalForm
# Create your views here.

class PersonalListView(ListView):
    template_name = 'admins/personal.html'
    context_object_name = 'personal'
    paginate_by = 7

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        order = self.request.GET.get("order", '')
        queryset = Personal.objects.buscar_personal(kword, order)
        return queryset


class PersonalUpdateView(UpdateView):
    template_name = 'admins/form_personal.html'
    model = Personal
    form_class = DiasForm
    success_url = reverse_lazy('admins_app:personal')


class PersonalCreateview(FormView):
    template_name = 'admins/form_personal.html'
    form_class = HospitalForm
    success_url = reverse_lazy('admins_app:personal')

    def form_valid(self, form):
        nombre = form.cleaned_data['nombre']
        user = self.request.user
        obj, created = Hospital.objects.get_or_create(
            nombre = nombre,
            user = user
        )
        return super(PersonalCreateview, self).form_valid(form)
