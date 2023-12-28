from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Task

class TaskAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task_data = {'title': 'Test Task', 'description': 'Test Description', 'status': 'Pending'}
        self.task = Task.objects.create(**self.task_data)
        self.task_id = self.task.id
        self.task_data['id'] = self.task_id

    def test_get_task_list(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        response = self.client.post('/api/tasks/', self.task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_task_detail(self):
        response = self.client.get(f'/api/tasks/{self.task_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_task(self):
        updated_data = {'title': 'Updated Task', 'description': 'Updated Description', 'status': 'Completed'}
        response = self.client.put(f'/api/tasks/{self.task_id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.get(id=self.task_id).title, updated_data['title'])

    def test_delete_task(self):
        response = self.client.delete(f'/api/tasks/{self.task_id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(id=self.task_id)

