from django.urls import path
from . import views


app_name = "personal_app"

urlpatterns = [
   path('', views.BusquedaPersonalListView.as_view(), name='busqueda',),
   path('personal/', views.PersonalListView.as_view(), name='personal',),
   path('personal/crear/', views.PersonalCreateview.as_view(), name='perso-nuevo',),
   path('personal/editar/<pk>/', views.PersonalUpdateView.as_view(), name='perso-update',),
]
