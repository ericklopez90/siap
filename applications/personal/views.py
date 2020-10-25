from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    View,
    UpdateView,
    DeleteView,
    DeleteView,
    ListView,
    TemplateView
)
from django.views.generic.edit import (
    FormView
)

from .models import Personal
# Create your views here.



