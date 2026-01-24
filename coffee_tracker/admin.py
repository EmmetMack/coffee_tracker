from django.contrib import admin
from .models import Roaster, BeanBag, BrewMethod, Recipe, Cup
# Register your models here.
admin.site.register(Roaster)
admin.site.register(BeanBag)
admin.site.register(BrewMethod)
admin.site.register(Recipe)
admin.site.register(Cup)