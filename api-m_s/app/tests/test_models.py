from django.test import TestCase

from app.models import User, Task


class TestUserModel(TestCase):
    '''test class for Users
    '''
    def setUp(self):
        self.user = User(name="Elmer")
        self.user.save()

    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 1)

    def test_user_representation(self):
        self.assertEqual(self.user.name, str(self.user))

class TestTaskModel(TestCase):
    '''test class for users Tasks
    '''
    def setUp(self):
        self.user = User(name="NN")
        self.user.save()
        self.task = self.user.task.create(description="Make the tests")
        self.task.save()

    def test_task_creation(self):
        self.assertEqual(Task.objects.count(), 1)

    def test_task_representation(self):
        self.assertEqual(self.task.description, str(self.task))