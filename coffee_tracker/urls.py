from django.urls import path
from .views import RoasterListView

urlpatterns = [
    path('roasters/', RoasterListView.as_view(), name='roaster-list'),
]