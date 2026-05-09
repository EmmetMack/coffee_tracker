from django.views.generic import ListView, TemplateView, DetailView
from .models import Roaster, BeanBag, BrewMethod, Recipe, Cup


class HomeView(TemplateView):
    template_name = 'coffee_tracker/home.html'


class RoasterListView(ListView):
    model = Roaster
    template_name = 'coffee_tracker/roaster_list.html'
    context_object_name = 'roasters'

class BeanBagListView(ListView):
    model = BeanBag
    template_name = 'coffee_tracker/beanbag_list.html'
    context_object_name = 'bean_bags'

class BrewMethodListView(ListView):
    model = BrewMethod
    template_name = 'coffee_tracker/brewmethod_list.html'
    context_object_name = 'brew_methods'

class RecipeListView(ListView):
    model = Recipe
    template_name = 'coffee_tracker/recipe_list.html'
    context_object_name = 'recipes'

class CupListView(ListView):
    model = Cup
    template_name = 'coffee_tracker/cup_list.html'
    context_object_name = 'cups'


class RoasterDetailView(DetailView):
    model = Roaster
    template_name = 'coffee_tracker/roaster_detail.html'
    context_object_name = 'roaster'

class BeanBagDetailView(DetailView):
    model = BeanBag
    template_name = 'coffee_tracker/beanbag_detail.html'
    context_object_name = 'bean_bag'

class BrewMethodDetailView(DetailView):
    model = BrewMethod
    template_name = 'coffee_tracker/brewmethod_detail.html'
    context_object_name = 'brew_method'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'coffee_tracker/recipe_detail.html'
    context_object_name = 'recipe'

class CupDetailView(DetailView):
    model = Cup
    template_name = 'coffee_tracker/cup_detail.html'
    context_object_name = 'cup'

