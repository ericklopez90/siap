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

from .forms import FaltasForm
from .models import Faltas
from applications.personal.models import Personal
from applications.personal.managers import PersonalManager

# Create your views here.

class FaltasCreateview(FormView):
    template_name = 'controlasist/form_faltas.html'
    model = Personal
    form_class = FaltasForm
    success_url = '.'

    def form_valid(self, form):
        fecha = form.cleaned_data['fecha']
        falta = form.cleaned_data['falta']
        personal = Personal.objects.get(id=self.kwargs['pk'])
        user = self.request.user
        obj, created = Faltas.objects.get_or_create(
            fecha = fecha,
            falta = falta,
            personal = personal,
            user = user
        )
        return super(FaltasCreateview, self).form_valid(form)

class FaltasUpdateView(UpdateView):
    template_name = 'controlasist/form_faltas.html'
    model = Personal
    form_class = FaltasForm
    success_url = '.'


class PruebaFaltas(TemplateView):
    template_name = 'controlasist/pruebafaltas.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['faltas'] = Personal.objects.buscar_faltasporpersonal()
        context['faltass'] = Personal.objects.buscar_faltasporpersonall()
        return context