from django.test import TestCase
from django.urls import reverse

class SnacksTests(TestCase):
    def test_home_page(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(url, '/')
    
    def test_snack_details_page(self):
        url = reverse('snack_detail',args=[1])
        response = self.client.get(url)
        self.assertEqual(url, '/1/')
        self.assertEqual(response.status_code, 404)
