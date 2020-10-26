from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    View,
    UpdateView,
    DeleteView,
    ListView,
    TemplateView,
    CreateView
)
from django.views.generic.edit import (
    FormView
)

from .models import (
    Universo,
    ZonaPagadora,
    SeccionSindical,
    Prestaciones,
    TipoContratacion,
    NivelSalarial,
    CodigoPuesto,
    Turno,
    Dias
)

from .forms import (
    UniversoForm,
    ZonaPagadoraForm,
    SeccionSindicalForm,
    PrestacionesForm,
    TipoContratacionForm,
    NivelSalarialForm,
    CodigoPuestoForm,
    TurnoForm,
    DiasForm
)

from .functions import registrar_nuevo_uni
# Create your views here.


class BaseView(TemplateView):
    template_name = "personal/busqueda.html"

class CatalogosView(FormView):
    template_name = 'personal/catalogos.html'
    form_class = UniversoForm
    success_url = '.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['universo'] = UniversoForm
        context['zona_pagadora'] = ZonaPagadoraForm
        context['seccion_sindical'] = SeccionSindicalForm
        context['prestaciones'] = PrestacionesForm
        context['tipo_de_contratacion'] = TipoContratacionForm
        context['nivel_salarial'] = NivelSalarialForm
        context['codigo_puesto'] = CodigoPuestoForm
        context['Turno'] = TurnoForm
        context['Dias'] = DiasForm
        return context

class UniversoListView(ListView):
    template_name = 'admins/universo.html'
    model = Universo
    context_object_name = 'universo'
    paginate_by = 10

class UniversoCreateview(FormView):
    template_name = 'admins/form_universo.html'
    form_class = UniversoForm
    success_url = reverse_lazy('admins_app:universo')


    def form_valid(self, form):
        nombre = form.cleaned_data['nombre']
        user = self.request.user
        obj, created = Universo.objects.get_or_create(
            nombre = nombre,
            user = user
        )
        return super(UniversoCreateview, self).form_valid(form)