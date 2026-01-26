from django.urls import path
from .views import RoasterListView, BeanBagListView

urlpatterns = [
    path('roasters/', RoasterListView.as_view(), name='roaster-list'),
    path('beans', BeanBagListView.as_view(), name='beanbag-list'),
]