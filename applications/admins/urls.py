from django.urls import path
from . import views

app_name = "admin_app"

urlpatterns = [
    path('', views.UniversoListView.as_view(), name='base',),
]
