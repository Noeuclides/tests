from django.shortcuts import reverse

from rest_framework.test import APITestCase

from app.models import User, Task


class TestNoteApi(APITestCase):
    def setUp(self):
        # create user
        self.user = User(name="Betty")
        self.user.save()

    def test_user_creation(self):
        response = self.client.post(reverse('user'), {
            'name': 'Ernesto',
        })

        # assert new user was added
        self.assertEqual(User.objects.count(), 2)

        # assert a created status code was returned
        self.assertEqual(201, response.status_code)

    def test_getting_user(self):
        response = self.client.get(reverse('user'), format="json")
        self.assertEqual(len(response.data), 1)

    def test_updating_user(self):
        response = self.client.put(reverse('detail', kwargs={"pk": 1}), {
            'name': 'Franz',
            'task': [],
        }, format="json")

        # check info returned has the update
        self.assertEqual('Franz', response.data['name'])

    def test_deleting_user(self):
        response = self.client.delete(reverse('detail', kwargs={"pk": 1}))

        self.assertEqual(204, response.status_code)

class TestViewApi(APITestCase):
    def setUp(self):
        # create task for user
        self.user = User(name="NN")
        self.user.save()
        self.task = self.user.task.create(description="Make Tests for view")
        self.task.save()

    def test_task_creation(self):
        response = self.client.post(reverse('task'), {
            'description': 'Make views',
            'state': 'True',
            'user_id': 1
        })

        # assert new task was added
        self.assertEqual(Task.objects.count(), 2)

        # assert a created status code was returned
        self.assertEqual(201, response.status_code)

    def test_getting_user(self):
        self.assertEqual(Task.objects.get(pk=1).user_id, self.user)     

    def test_updating_user(self):
        response = self.client.put(reverse('task_detail', kwargs={"pk": 1}), {
            'description': 'Make models',
            'user_id': 1
        }, format="json")

        # check info returned has the update
        self.assertEqual('Make models', response.data['description'])

    def test_deleting_user(self):
        response = self.client.delete(reverse('task_detail', kwargs={"pk": 1}))

        self.assertEqual(204, response.status_code)