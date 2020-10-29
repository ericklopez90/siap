from django.urls import path
from . import views

app_name = "admins_app"

urlpatterns = [
    path('catalogo/', views.CatalogoView.as_view(), name='catalogo',),
    path('catalogo/dias/', views.DiasListView.as_view(), name='dias',),
    path('catalogo/dias/crear/', views.DiasCreateview.as_view(), name='diasnuevo',),
    path('catalogo/dias/editar/<pk>/', views.DiasUpdateView.as_view(), name='dias-update',),
    path('catalogo/codigop/', views.CodigoPuestoListView.as_view(), name='codigop',),
    path('catalogo/codigop/crear/', views.CodigoPuestoCreateview.as_view(), name='codigopnuevo',),
    path('catalogo/codigop/editar/<pk>/', views.CodigoPuestoUpdateView.as_view(), name='codigop-update',),
    path('catalogo/nivels/', views.NivelSalarialListView.as_view(), name='nivels',),
    path('catalogo/nivels/crear/', views.NivelSalarialCreateview.as_view(), name='nivelsnuevo',),
    path('catalogo/nivels/editar/<pk>/', views.NivelSalarialUpdateView.as_view(), name='nivels-update',),
    path('catalogo/seccions/', views.SeccionSindicalListView.as_view(), name='seccions',),
    path('catalogo/seccions/crear/', views.SeccionSindicalCreateview.as_view(), name='seccionsnuevo',),
    path('catalogo/seccions/editar/<pk>/', views.SeccionSindicalUpdateView.as_view(), name='seccions-update',),
    path('catalogo/universo/', views.UniversoListView.as_view(), name='universo',),
    path('catalogo/universo/crear/', views.UniversoCreateview.as_view(), name='uninuevo',),
    path('catalogo/universo/editar/<pk>/', views.UniversoUpdateView.as_view(), name='uni-update',),
    path('catalogo/zonap/', views.ZonaPagadoraListView.as_view(), name='zonap',),
    path('catalogo/zonap/crear/', views.ZonaPagadoraCreateview.as_view(), name='zonapnuevo',),
    path('catalogo/zonap/editar/<pk>/', views.ZonaPagadoraUpdateView.as_view(), name='zonap-update',),
    path('catalogo/tipoc/', views.TipoContratacionListView.as_view(), name='tipoc',),
    path('catalogo/tipoc/crear/', views.TipoContratacionCreateview.as_view(), name='tipocnuevo',),
    path('catalogo/tipoc/editar/<pk>/', views.TipoContratacionUpdateView.as_view(), name='tipoc-update',),
    path('catalogo/hospital/', views.HospitalListView.as_view(), name='hospital',),
    path('catalogo/hospital/crear/', views.HospitalCreateview.as_view(), name='hospinuevo',),
    path('catalogo/hospital/editar/<pk>/', views.HospitalUpdateView.as_view(), name='hospi-update',),
    path('catalogo/turno/', views.TurnoListView.as_view(), name='turno',),
    path('catalogo/turno/crear/', views.TurnoCreateview.as_view(), name='turnonuevo',),
    path('catalogo/turno/editar/<pk>/', views.TurnoUpdateView.as_view(), name='turno-update',),
    path('catalogo/prestaciones/', views.PrestacionesListView.as_view(), name='prestaciones',),
    path('catalogo/prestaciones/crear/', views.PrestacionesCreateview.as_view(), name='prestanuevo',),
    path('catalogo/prestaciones/editar/<pk>/', views.PrestacionesUpdateView.as_view(), name='presta-update',),
]
