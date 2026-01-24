from django.shortcuts import render
from django.views.generic import ListView
from .models import Roaster
# Create your views here.

class RoasterListView(ListView):
    model = Roaster
    template_name = 'coffee_tracker/roaster_list.html'
    context_object_name = 'roasters'

