from django.urls import path
from .views import (
    HomeView,
    RoasterListView, RoasterDetailView,
    BeanBagListView, BeanBagDetailView,
    BrewMethodListView, BrewMethodDetailView,
    RecipeListView, RecipeDetailView,
    CupListView, CupDetailView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('roasters/', RoasterListView.as_view(), name='roaster-list'),
    path('roasters/<int:pk>/', RoasterDetailView.as_view(), name='roaster-detail'),
    path('beans/', BeanBagListView.as_view(), name='beanbag-list'),
    path('beans/<int:pk>/', BeanBagDetailView.as_view(), name='beanbag-detail'),
    path('brew-methods/', BrewMethodListView.as_view(), name='brewmethod-list'),
    path('brew-methods/<int:pk>/', BrewMethodDetailView.as_view(), name='brewmethod-detail'),
    path('recipes/', RecipeListView.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('cups/', CupListView.as_view(), name='cup-list'),
    path('cups/<int:pk>/', CupDetailView.as_view(), name='cup-detail'),
]