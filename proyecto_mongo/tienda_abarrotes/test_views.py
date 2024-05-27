from django.test import TestCase
from django.urls import reverse

class RedirectTest(TestCase):
    def test_redirect_to_inicio_page(self):
        response = self.client.get(reverse('inicio'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/inicio/')