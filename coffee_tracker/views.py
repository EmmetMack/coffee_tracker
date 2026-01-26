from django.shortcuts import render
from django.views.generic import ListView
from .models import Roaster, BeanBag
# Create your views here.

class RoasterListView(ListView):
    model = Roaster
    template_name = 'coffee_tracker/roaster_list.html'
    context_object_name = 'roasters'

class BeanBagListView(ListView):
    model = BeanBag
    template_name = 'coffee_tracker/bean_bag_list.html'
    context_object_name = 'bean_bags'

