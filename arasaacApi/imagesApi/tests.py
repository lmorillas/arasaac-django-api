from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from arasaacApi.imagesApi.models import  Image_en, Image_es

from rest_framework.test import APIRequestFactory

# Using the standard RequestFactory API to create a form POST request

connect('mongoenginetest', host='mongomock://localhost')

factory = APIRequestFactory()
request = factory.post('/notes/', {'title': 'new idea'})


class AccountTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('account-list')
        data = {'name': 'DabApps'}
        response = self.client.post(url, data, format='json')
        #self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #self.assertEqual(Account.objects.count(), 1)
        #self.assertEqual(Account.objects.get().name, 'DabApps')


from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from pollsapi import views

class TestPoll(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.PollList.as_view()
        self.uri = '/polls/'
    def test_get(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 200, 'Expected Response Code 200, received {0} instead.'
            .format(response.status_code))