import json
import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db
"""
pytest a_directory                     # directory
pytest test_something.py               # tests file
pytest test_something.py::single_test  # single test function
"""


@pytest.fixture
def authentication_user(client, django_user_model):
    """
    creating user id for note app crud operation testing
    :param client:
    :param django_user_model:
    :return:
    """
    user = django_user_model.objects.create_user(username='ronit', password='7777', phone_number=1234567890,
                                                 location='odisha')
    url = reverse('login')
    data = {'username': 'ronit', 'password': '7777'}
    client.post(url, data)
    return user.id


class TestNoteAppCrudOperation:
    """
    Test Crud Operation of Note
    """

    @pytest.mark.django_db
    def test_post_user_with_success_response(self, client, django_user_model, authentication_user):
        """
        Test post api
        :param client:
        :param django_user_model:
        :param authentication_user:
        :return:
        """
        user_id = authentication_user
        url = reverse("notedetails")
        data = {"title": "tea", "description": "famous in india", "user": user_id}
        response = client.post(url, data, content_type='application/json')
        assert response.status_code == 201

    @pytest.mark.django_db
    def test_note_get_api_response(self, client, authentication_user):
        """
        Test get api
        :param client:
        :param authentication_user:
        :return:
        """
        user_id = authentication_user
        # create note
        url = reverse("notedetails")
        data = {"title": "masala tea", "description": "famous in india", "user": user_id}
        response = client.post(url, data, content_type='application/json')
        assert response.status_code == 201
        # get note
        url = reverse('notedetails')
        url = url + '?user_id=' + str(user_id)
        response = client.get(url, content_type='application/json')
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_note_put_api_response(self, client, authentication_user):
        """
        Test put api
        :param client:
        :param authentication_user:
        :return:
        """
        user_id = authentication_user
        # new note
        url = reverse("notedetails")
        data = {"title": "tea", "description": "famous in india", "user": user_id}
        response = client.post(url, data, content_type='application/json')
        json_data = json.loads(response.content)
        note_id = json_data.get('data').get('id')
        assert response.status_code == 201
        # update note
        url = reverse("notedetails")
        data = {"id": note_id, "title": "coffee", "description": "Nestle", "user": user_id}
        response = client.put(url, data, content_type='application/json')
        # json_data = json.loads(response.content)
        # print(json_data)
        assert response.status_code == 201

    @pytest.mark.django_db
    def test_note_delete_response(self, client, authentication_user):
        """
        Test delete api
        :param client:
        :param authentication_user:
        :return:
        """
        user_id = authentication_user
        # new note
        url = reverse('notedetails')
        data = {'title': 'chips', 'description': 'lays', "user": user_id}
        response = client.post(url, data, content_type='application/json')
        json_data = json.loads(response.content)
        assert response.status_code == 201
        note_id = json_data.get('data').get('id')
        # Delete notes
        url = reverse("notedetails")
        data = {'id': note_id}
        response = client.delete(url, data, content_type='application/json')
        assert response.status_code == 204
        assert response.data == {'data': 'deleted'}
