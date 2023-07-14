from django.test import TestCase, RequestFactory, Client
from django.urls import reverse
from ..forms import BookTableForm, CartForm
from ..views import CartView, CustomerView, BookView
from ..models import Table, Order, Receipt, Order_menuItem


# class TestUserRegisterView(TestCase):
#     def setUp(self):
#         self.client = Client()

#     def test_user_register_GET(self):
#         response = self.client.get(reverse('home:user_register'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'home/register.html')
#         self.failUnless(response.context['form'], UserRegistrationForm)

#     def test_user_register_POST_valid(self):
#         response = self.client.post(reverse('home:user_register'),
#                                     data={'username': 'Kevin', 'email': 'kevin@email.com', 'password1': 'kevinpass',
#                                           'password2': 'kevinpass'})
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, reverse('home:home'))
#         self.assertEqual(User.objects.count(), 1)

#     def test_user_register_POST_invalid(self):
#         response = self.client.post(reverse('home:user_register'),
#                                     data={'username': 'jack', 'email': 'invalid_email', 'password1': 'jackpass',
#                                           'password2': 'jackpass'})
#         self.assertEqual(response.status_code, 200)
#         self.failIf(response.context['form'].is_valid())
#         self.assertFormError(form=response.context['form'], field='email', errors=['Enter a valid email address.'])


# class TestWriterViews(TestCase):
#     def setUp(self):
#         User.objects.create_user(username='root', email='root@email.com', password='rootpass')
#         self.client = Client()
#         self.client.login(username='root', email='root@email.com', password='rootpass')

#     def test_writers(self):
#         response = self.client.get(reverse('home:writers'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'home/writers.html')


# class TestHomeView(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='root', email='root@email.com', password='rootpass')
#         self.factory = RequestFactory()

#     def test_home_user_authenticated(self):
#         request = self.factory.get(reverse('home:home'))
#         request.user = self.user
#         response = Home.as_view()(request)
#         self.assertEqual(response.status_code, 302)

#     def test_home_user_anonymous(self):
#         request = self.factory.get(reverse('home:home'))
#         request.user = AnonymousUser()
#         response = Home.as_view()(request)
#         self.assertEqual(response.status_code, 200)
class TestCartView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_cart_GET(self):
        response = self.client.get(reverse('cart'))
        self.assertTemplateUsed(response, 'cart.html')
        # self.assertEqual(response.status_code, 200)
        # self.failUnless(response.context['form'], CartForm)

    def test_cart_POST_valid(self):
        table= Table.objects.create(number=100, space_position='center', capacity=5)
        response = self.client.post(reverse('cart'), data={'table': table, 'phone_number':'09129285768'})
        valid_form=response.context['form'].is_valid()
        self.assertTrue(valid_form)
        # self.assertEqual(Order.objects.count(), 1)
        # self.assertEqual(Receipt.objects.count(), 1)
        # self.assertEqual(response.status_code, 302)
        # self.assertRedirects(response, reverse('customer'))
#         self.failIf(response.context['form'].is_valid())
#         self.assertFormError(form=response.context['form'], field='email', errors=['Enter a valid email address.'])



class TestCustomerView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_customer_GET(self):
        response = self.client.get(reverse('customer'))
        self.assertTemplateUsed(response, 'customer.html')
        self.assertEqual(response.status_code, 200)
        # self.failUnless(response.context['orders'], )



