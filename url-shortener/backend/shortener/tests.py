from django.test import TestCase
from .models import ShortenedURL

class ShortenedURLModelTest(TestCase):
    def setUp(self):
        self.url = ShortenedURL.objects.create(original_url='https://www.example.com', shortened_url='exmpl')

    def test_shortened_url_creation(self):
        self.assertEqual(self.url.original_url, 'https://www.example.com')
        self.assertEqual(self.url.shortened_url, 'exmpl')

    def test_shortened_url_retrieval(self):
        retrieved_url = ShortenedURL.objects.get(shortened_url='exmpl')
        self.assertEqual(retrieved_url.original_url, 'https://www.example.com')