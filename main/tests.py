from django.test import TestCase
from django.urls import reverse


class MainSimpleViewTests(TestCase):
    def test_home_status_ok(self):
        response = self.client.get(reverse('main:home'))
        self.assertEqual(response.status_code, 200)

    def test_about_status_ok(self):
        response = self.client.get(reverse('main:about'))
        self.assertEqual(response.status_code, 200)

    def test_projects_status_ok(self):
        response = self.client.get(reverse('main:projects'))
        self.assertEqual(response.status_code, 200)

    def test_contact_status_ok(self):
        response = self.client.get(reverse('main:contact'))
        self.assertEqual(response.status_code, 200)
