from django.test import TestCase
from django.urls import reverse
from .models import Post


class IndexViewTests(TestCase):
    def test_index_status_ok(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_index_shows_post(self):
        post = Post.objects.create(title='Test Post', content='Content')
        response = self.client.get(reverse('index'))
        self.assertContains(response, 'Test Post')
