from django.urls import path
from .views import RoasterListView, BeanBagListView, BrewMethodListView, RecipeListView, CupListView

urlpatterns = [
    path('roasters/', RoasterListView.as_view(), name='roaster-list'),
    path('beans/', BeanBagListView.as_view(), name='beanbag-list'),
    path('brew-methods/', BrewMethodListView.as_view(), name='brewmethod-list'),
    path('recipes/', RecipeListView.as_view(), name='recipe-list'),
    path('cups/', CupListView.as_view(), name='cup-list'),
]