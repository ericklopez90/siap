from django.urls import path
from . import views

app_name = "admins_app"

urlpatterns = [
    path('', views.UniversoListView.as_view(), name='universo',),
    path('crear/', views.UniversoCreateview.as_view(), name='uninuevo',),
]
