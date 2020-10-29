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
    Dias,
    Hospital
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
    DiasForm,
    HospitalForm
)

from .functions import registrar_nuevo_uni
# Create your views here.


class CatalogoView(TemplateView):
    template_name = "admins/catalogo.html"

class DiasListView(ListView):
    template_name = 'admins/dias.html'
    context_object_name = 'dias'
    paginate_by = 7

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        order = self.request.GET.get("order", '')
        queryset = Dias.objects.buscar_dias(kword, order)
        return queryset


class DiasUpdateView(UpdateView):
    template_name = 'admins/form_dias.html'
    model = Dias
    form_class = DiasForm
    success_url = reverse_lazy('admins_app:dias')


class DiasCreateview(FormView):
    template_name = 'admins/form_dias.html'
    form_class = DiasForm
    success_url = reverse_lazy('admins_app:dias')

    def form_valid(self, form):
        nombre = form.cleaned_data['nombre']
        user = self.request.user
        obj, created = Dias.objects.get_or_create(
            nombre = nombre,
            user = user
        )
        return super(DiasCreateview, self).form_valid(form)

class CodigoPuestoListView(ListView):
    template_name = 'admins/codigopuesto.html'
    context_object_name = 'codigopuesto'
    paginate_by = 5

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        order = self.request.GET.get("order", '')
        queryset = CodigoPuesto.objects.buscar_codigopuesto(kword, order)
        return queryset


class CodigoPuestoUpdateView(UpdateView):
    template_name = 'admins/form_codigopuesto.html'
    model = CodigoPuesto
    form_class = CodigoPuestoForm
    success_url = reverse_lazy('admins_app:codigop')


class CodigoPuestoCreateview(FormView):
    template_name = 'admins/form_codigopuesto.html'
    form_class = CodigoPuestoForm
    success_url = reverse_lazy('admins_app:codigop')

    def form_valid(self, form):
        nombre = form.cleaned_data['nombre']
        user = self.request.user
        obj, created = CodigoPuesto.objects.get_or_create(
            nombre = nombre,
            user = user
        )
        return super(CodigoPuestoCreateview, self).form_valid(form)

class NivelSalarialListView(ListView):
    template_name = 'admins/nivelsalarial.html'
    context_object_name = 'nivelsalarial'
    paginate_by = 5

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        order = self.request.GET.get("order", '')
        queryset = NivelSalarial.objects.buscar_nivelsalarial(kword, order)
        return queryset


class NivelSalarialUpdateView(UpdateView):
    template_name = 'admins/form_nivelsalarial.html'
    model = NivelSalarial
    form_class = NivelSalarialForm
    success_url = reverse_lazy('admins_app:nivels')


class NivelSalarialCreateview(FormView):
    template_name = 'admins/form_nivelsalarial.html'
    form_class = NivelSalarialForm
    success_url = reverse_lazy('admins_app:nivels')

    def form_valid(self, form):
        nivel = form.cleaned_data['nivel']
        user = self.request.user
        obj, created = NivelSalarial.objects.get_or_create(
            nivel = nivel,
            user = user
        )
        return super(NivelSalarialCreateview, self).form_valid(form)

class SeccionSindicalListView(ListView):
    template_name = 'admins/seccionsindical.html'
    context_object_name = 'seccionsindical'
    paginate_by = 5

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        order = self.request.GET.get("order", '')
        queryset = SeccionSindical.objects.buscar_seccionsindical(kword, order)
        return queryset


class SeccionSindicalUpdateView(UpdateView):
    template_name = 'admins/form_seccionsindical.html'
    model = SeccionSindical
    form_class = SeccionSindicalForm
    success_url = reverse_lazy('admins_app:seccions')


class SeccionSindicalCreateview(FormView):
    template_name = 'admins/form_seccionsindical.html'
    form_class = SeccionSindicalForm
    success_url = reverse_lazy('admins_app:seccions')

    def form_valid(self, form):
        nombre = form.cleaned_data['nombre']
        seccion = form.cleaned_data['seccion']
        user = self.request.user
        obj, created = SeccionSindical.objects.get_or_create(
            nombre = nombre,
            user = user,
            seccion = seccion
        )
        return super(SeccionSindicalCreateview, self).form_valid(form)


class UniversoListView(ListView):
    template_name = 'admins/universo.html'
    context_object_name = 'universo'
    paginate_by = 5

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        order = self.request.GET.get("order", '')
        queryset = Universo.objects.buscar_universo(kword, order)
        return queryset


class UniversoUpdateView(UpdateView):
    template_name = 'admins/form_universo.html'
    model = Universo
    form_class = UniversoForm
    success_url = reverse_lazy('admins_app:universo')


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


class ZonaPagadoraListView(ListView):
    template_name = 'admins/zonapagadora.html'
    context_object_name = 'zonapagadora'
    paginate_by = 5

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        order = self.request.GET.get("order", '')
        queryset = ZonaPagadora.objects.buscar_zonapagadora(kword, order)
        return queryset


class ZonaPagadoraUpdateView(UpdateView):
    template_name = 'admins/form_zonapagadora.html'
    model = ZonaPagadora
    form_class = ZonaPagadoraForm
    success_url = reverse_lazy('admins_app:zonap')


class ZonaPagadoraCreateview(FormView):
    template_name = 'admins/form_zonapagadora.html'
    form_class = ZonaPagadoraForm
    success_url = reverse_lazy('admins_app:zonap')

    def form_valid(self, form):
        nombre = form.cleaned_data['nombre']
        user = self.request.user
        obj, created = ZonaPagadora.objects.get_or_create(
            nombre = nombre,
            user = user
        )
        return super(ZonaPagadoraCreateview, self).form_valid(form)

    
class TipoContratacionListView(ListView):
    template_name = 'admins/tipocontratacion.html'
    context_object_name = 'tipocontratacion'
    paginate_by = 5

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        order = self.request.GET.get("order", '')
        queryset = TipoContratacion.objects.buscar_tipocontratacion(kword, order)
        return queryset


class TipoContratacionUpdateView(UpdateView):
    template_name = 'admins/form_tipocontratacion.html'
    model = TipoContratacion
    form_class = TipoContratacionForm
    success_url = reverse_lazy('admins_app:tipoc')


class TipoContratacionCreateview(FormView):
    template_name = 'admins/form_tipocontratacion.html'
    form_class = TipoContratacionForm
    success_url = reverse_lazy('admins_app:tipoc')

    def form_valid(self, form):
        nombre = form.cleaned_data['nombre']
        user = self.request.user
        obj, created = TipoContratacion.objects.get_or_create(
            nombre = nombre,
            user = user
        )
        return super(TipoContratacionCreateview, self).form_valid(form)


class HospitalListView(ListView):
    template_name = 'admins/hospital.html'
    context_object_name = 'hospital'
    paginate_by = 5

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        order = self.request.GET.get("order", '')
        queryset = Hospital.objects.buscar_hospital(kword, order)
        return queryset


class HospitalUpdateView(UpdateView):
    template_name = 'admins/form_hospital.html'
    model = Hospital
    form_class = HospitalForm
    success_url = reverse_lazy('admins_app:hospital')


class HospitalCreateview(FormView):
    template_name = 'admins/form_hospital.html'
    form_class = HospitalForm
    success_url = reverse_lazy('admins_app:hospital')

    def form_valid(self, form):
        nombre = form.cleaned_data['nombre']
        user = self.request.user
        obj, created = Hospital.objects.get_or_create(
            nombre = nombre,
            user = user
        )
        return super(HospitalCreateview, self).form_valid(form)

class TurnoListView(ListView):
    template_name = 'admins/turno.html'
    context_object_name = 'turno'
    paginate_by = 5

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        order = self.request.GET.get("order", '')
        queryset = Turno.objects.buscar_turno(kword, order)
        return queryset


class TurnoUpdateView(UpdateView):
    template_name = 'admins/form_turno.html'
    model = Turno
    form_class = TurnoForm
    success_url = reverse_lazy('admins_app:turno')


class TurnoCreateview(FormView):
    template_name = 'admins/form_turno.html'
    form_class = TurnoForm
    success_url = reverse_lazy('admins_app:turno')

    def form_valid(self, form):
        nombre = form.cleaned_data['nombre']
        dia_trab = form.cleaned_data['dia_trab']
        user = self.request.user
        obj, created = Turno.objects.get_or_create(
            nombre = nombre,
            user = user,
            dia_trab = dia_trab
        )
        return super(TurnoCreateview, self).form_valid(form)


class PrestacionesListView(ListView):
    template_name = 'admins/prestaciones.html'
    context_object_name = 'prestaciones'
    paginate_by = 5

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        order = self.request.GET.get("order", '')
        queryset = Prestaciones.objects.buscar_prestaciones(kword, order)
        return queryset


class PrestacionesUpdateView(UpdateView):
    template_name = 'admins/form_prestaciones.html'
    model = Prestaciones
    form_class = PrestacionesForm
    success_url = reverse_lazy('admins_app:prestaciones')


class PrestacionesCreateview(FormView):
    template_name = 'admins/form_prestaciones.html'
    form_class = PrestacionesForm
    success_url = reverse_lazy('admins_app:prestaciones')

    def form_valid(self, form):
        nombre = form.cleaned_data['nombre']
        num_dias = form.cleaned_data['num_dias']
        turno = form.cleaned_data['turno']
        user = self.request.user
        obj, created = Prestaciones.objects.get_or_create(
            nombre = nombre,
            user = user,
            num_dias = num_dias,
            turno = turno
        )
        return super(PrestacionesCreateview, self).form_valid(form)