from django.urls import path
from . import views

app_name = "controlasist_app"

urlpatterns = [
    path('falta/<pk>/', views.FaltasCreateview.as_view(), name='falta'),
    path('falta/', views.PruebaFaltas.as_view(), name='faltaaaa'),
]
