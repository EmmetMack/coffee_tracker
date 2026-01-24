from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Roaster(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    website = models.URLField(blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class BeanBag(models.Model):
    roaster = models.ForeignKey(Roaster, on_delete=models.CASCADE, related_name='bean_bags')
    name = models.CharField(max_length=200)
    origin = models.CharField(max_length=200, blank=True)
    roast_date = models.DateField(null=True, blank=True)
    roast_level = models.CharField(max_length=30, blank=True)
    tasting_notes = models.TextField(blank=True)
    comments = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} by {self.roaster.name}"
    

class BrewMethod(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    brew_method = models.ForeignKey(BrewMethod, on_delete=models.CASCADE, related_name='recipes')
    coffee_dose = models.FloatField(help_text="Amount of coffee in grams")
    water_dose = models.FloatField(help_text="Amount of water in milliliters")
    grind_size_description = models.CharField(max_length=200, blank=True, help_text="Recommended grind size description")
    grind_size_numeric = models.IntegerField(null=True, blank=True, help_text="Recommended numeric grind size if applicable")
    temp = models.FloatField(help_text="Brewing temperature", blank=True, null=True)
    temp_unit = models.CharField(max_length=1, choices=[('C', 'Celsius'), ('F', 'Fahrenheit')], default='F')
    instructions = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.brew_method.name})"
    

class Cup(models.Model):
    bean_bag = models.ForeignKey(BeanBag, on_delete=models.SET_NULL, null=True, related_name='cups')
    recipe = models.ForeignKey(Recipe, on_delete=models.SET_NULL, null=True, related_name='cups')
    brew_date = models.DateTimeField(help_text="Date and time of brewing")
    grind_size_numeric = models.IntegerField(null=True, blank=True, help_text="Actual grind size used")
    water_temp = models.FloatField(null=True, blank=True, help_text="Actual water temperature")
    temp_unit = models.CharField(max_length=1, choices=[('C', 'Celsius'), ('F', 'Fahrenheit')], default='F')
    actual_coffee_dose = models.FloatField(null=True, blank=True, help_text="Actual amount of coffee used in grams")
    actual_water_dose = models.FloatField(null=True, blank=True, help_text="Actual amount of water used in milliliters")
    rating = models.IntegerField(null=True, blank=True, help_text="Rating from 1 to 10", validators=[MinValueValidator(1), MaxValueValidator(10)])
    recipe_variations = models.TextField(blank=True, help_text="Notes on any variations from recipe")
    tasting_notes = models.TextField(blank=True)
    grinder_name = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if not self.bean_bag:
            return f'Cup brewed on {self.brew_date.strftime("%Y-%m-%d %H:%M")}'
        return f'Cup of {self.bean_bag.name} brewed on {self.brew_date.strftime("%Y-%m-%d %H:%M")}'
