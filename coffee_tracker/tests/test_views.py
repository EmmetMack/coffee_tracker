from django.test import TestCase

from coffee_tracker.models import Roaster


class RoasterListViewTests(TestCase):
    def setUp(self):
        self.roaster = Roaster.objects.create(name="Intelligentsia")

    def test_roaster_list_returns_200(self):
        response = self.client.get("/roasters/")
        self.assertEqual(response.status_code, 200)

    def test_roaster_list_uses_correct_template(self):
        response = self.client.get("/roasters/")
        self.assertTemplateUsed(response, "coffee_tracker/roaster_list.html")

    def test_roaster_name_in_content(self):
        response = self.client.get("/roasters/")
        self.assertContains(response, "Intelligentsia")
