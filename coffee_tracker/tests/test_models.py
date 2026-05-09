from datetime import datetime, timezone as dt_timezone

from django.core.exceptions import ValidationError
from django.test import TestCase

from coffee_tracker.models import BeanBag, BrewMethod, Cup, Recipe, Roaster


class ModelStrTests(TestCase):
    def setUp(self):
        self.roaster = Roaster.objects.create(name="Blue Bottle")
        self.bag = BeanBag.objects.create(name="Ethiopia Yirgacheffe", roaster=self.roaster)
        self.method = BrewMethod.objects.create(name="Pour Over")
        self.recipe = Recipe.objects.create(
            name="My V60",
            brew_method=self.method,
            coffee_dose=15.0,
            water_dose=250.0,
        )
        self.brew_date = datetime(2024, 3, 1, 9, 0, tzinfo=dt_timezone.utc)
        self.cup_with_bag = Cup.objects.create(
            bean_bag=self.bag, brew_date=self.brew_date
        )
        self.cup_without_bag = Cup.objects.create(brew_date=self.brew_date)

    def test_roaster_str(self):
        self.assertEqual(str(self.roaster), "Blue Bottle")

    def test_beanbag_str(self):
        self.assertEqual(str(self.bag), "Ethiopia Yirgacheffe by Blue Bottle")

    def test_brewmethod_str(self):
        self.assertEqual(str(self.method), "Pour Over")

    def test_recipe_str(self):
        self.assertEqual(str(self.recipe), "My V60 (Pour Over)")

    def test_cup_str_with_bean_bag(self):
        self.assertIn("Ethiopia Yirgacheffe", str(self.cup_with_bag))

    def test_cup_str_without_bean_bag(self):
        result = str(self.cup_without_bag)
        self.assertIn("Cup brewed on", result)
        self.assertNotIn("None", result)


class RatingValidatorTests(TestCase):
    def setUp(self):
        self.brew_date = datetime(2024, 3, 1, 9, 0, tzinfo=dt_timezone.utc)

    def test_rating_rejects_below_1(self):
        cup = Cup(brew_date=self.brew_date, rating=0)
        with self.assertRaises(ValidationError):
            cup.full_clean()

    def test_rating_rejects_above_10(self):
        cup = Cup(brew_date=self.brew_date, rating=11)
        with self.assertRaises(ValidationError):
            cup.full_clean()


class ForeignKeyBehaviorTests(TestCase):
    def setUp(self):
        self.roaster = Roaster.objects.create(name="Stumptown")
        self.bag = BeanBag.objects.create(name="Hair Bender", roaster=self.roaster)
        brew_date = datetime(2024, 3, 1, 9, 0, tzinfo=dt_timezone.utc)
        self.cup = Cup.objects.create(bean_bag=self.bag, brew_date=brew_date)

    def test_roaster_cascade_deletes_beanbag(self):
        bag_pk = self.bag.pk
        self.roaster.delete()
        self.assertFalse(BeanBag.objects.filter(pk=bag_pk).exists())

    def test_beanbag_delete_sets_cup_null(self):
        self.bag.delete()
        self.cup.refresh_from_db()
        self.assertIsNone(self.cup.bean_bag)
