from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import CartView, CustomerView, BookView


class TestUrls(SimpleTestCase):
    def test_cart(self):
        url = reverse('cart')  
        # print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, CartView)

    def test_customer(self):
        url = reverse('customer')  
        # print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, CustomerView)

    def test_book(self):
        url = reverse('book')  
        # print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, BookView)