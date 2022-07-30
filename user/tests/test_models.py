import pytest
import json
from django.urls import reverse

pytestmark = pytest.mark.django_db
"""
pytest a_directory                     # directory
pytest test_something.py               # tests file
pytest test_something.py::single_test  # single test function
"""


class TestRegistrationAPI:
    """
    Test Registration and login API
    """
    @pytest.mark.django_db
    def test_response_as_login_successfully(self, client, django_user_model):
        """
        Test login success
        :param client:
        :param django_user_model:
        :return:
        """
        # Create user
        user = django_user_model.objects.create_user(username='ronit', password='7777', phone_number=1234567890,
                                                     location='odisha')
        url = reverse('login')
        # Login user
        data = {'username': 'ronit', 'password': '7777'}
        response = client.post(url, data, content_type="application/json")
        assert response.status_code == 200
        assert response.data['message'] == f'User {user.username} is successfully login'

    @pytest.mark.django_db
    def test_response_as_login_failure(self, client, django_user_model):
        """
        Test login failure
        :param client:
        :param django_user_model:
        :return:
        """

        # Create user
        django_user_model.objects.create_user(username='ronit', password='7777', phone_number=1234567890,
                                              location='odisha')
        url = reverse('login')
        # Login failed
        data = {'username': 'ronit', 'password': '123'}
        response = client.post(url, data, content_type="application/json")
        assert response.status_code == 401
        assert response.data['message'] == 'Invalid username/password'


