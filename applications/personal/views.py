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


class BusquedaPersonalListView(ListView):
    template_name = 'personal/busqueda.html'
    context_object_name = 'personal'
    paginate_by = 6

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        order = self.request.GET.get("order", '')
        queryset = Personal.objects.buscar_personal(kword, order)
        return queryset


class PersonalDetailView(TemplateView):
    template_name = 'personal/detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['faltas'] = faltas_por_personal
        context['personal'] = Personal.objects.all()
        return context


class PersonalListView(ListView):
    template_name = 'personal/personal.html'
    context_object_name = 'personal'
    paginate_by = 7

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        order = self.request.GET.get("order", '')
        queryset = Personal.objects.buscar_personal(kword, order)
        return queryset


class PersonalUpdateView(UpdateView):
    template_name = 'personal/form_personal.html'
    model = Personal
    form_class = PersonalForm
    success_url = reverse_lazy('personal_app:personal')


class PersonalCreateview(FormView):
    template_name = 'personal/form_personal.html'
    form_class = PersonalForm
    success_url = reverse_lazy('personal_app:personal')

    def form_valid(self, form):
        nombre = form.cleaned_data['nombre']
        apellido_materno = form.cleaned_data['apellido_materno']
        apellido_paterno = form.cleaned_data['apellido_paterno']
        fecha_nac = form.cleaned_data['fecha_nac']
        curp = form.cleaned_data['curp']
        rfc = form.cleaned_data['rfc']
        num_empleado = form.cleaned_data['num_empleado']
        num_plaza = form.cleaned_data['num_plaza']
        fecha_ingreso = form.cleaned_data['fecha_ingreso']
        universo = form.cleaned_data['universo']
        nivel = form.cleaned_data['nivel']
        zona_pagadora = form.cleaned_data['zona_pagadora']
        codigo_puesto = form.cleaned_data['codigo_puesto']
        secc_sindical = form.cleaned_data['secc_sindical']
        hospital = form.cleaned_data['hospital']
        turno = form.cleaned_data['turno']
        prestaciones = form.cleaned_data['prestaciones']
        tipo_contratacion = form.cleaned_data['tipo_contratacion']
        user = self.request.user
        obj, created = Personal.objects.get_or_create(
            nombre = nombre,
            apellido_materno = apellido_materno,
            apellido_paterno = apellido_paterno,
            fecha_nac = fecha_nac,
            curp = curp,
            rfc = rfc,
            num_empleado = num_empleado,
            num_plaza = num_plaza,
            fecha_ingreso = fecha_ingreso,
            universo = universo,
            nivel = nivel,
            zona_pagadora = zona_pagadora,
            codigo_puesto = codigo_puesto,
            secc_sindical = secc_sindical,
            hospital = hospital,
            turno = turno,
            prestaciones = prestaciones,
            tipo_contratacion = tipo_contratacion,
            user = user
        )
        return super(PersonalCreateview, self).form_valid(form)
