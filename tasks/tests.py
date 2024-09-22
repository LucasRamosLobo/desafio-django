from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Task

class TaskAPITestCase(APITestCase):

    def setUp(self):
        self.task1 = Task.objects.create(title="Task 1", description="Descrição da task 1")
        self.task2 = Task.objects.create(title="Task 2", description="Descrição da task 2")
        self.create_url = reverse('task-list')

    def test_create_task(self):
        data = {"title": "Nova Task", "description": "Descrição da nova task"}
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], "Task criada com sucesso.")
        self.assertEqual(response.data['data']['title'], "Nova Task")

    def test_list_tasks(self):
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_update_task(self):
        task_id = self.task1.id
        url = reverse('task-detail', kwargs={'pk': task_id})
        data = {"title": "Task 1 Atualizada", "description": "Descrição atualizada da task 1"}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Task 'Task 1 Atualizada' foi atualizada com sucesso.")
        self.assertEqual(response.data['data']['title'], "Task 1 Atualizada")

    def test_delete_task(self):
        task_id = self.task1.id
        url = reverse('task-detail', kwargs={'pk': task_id}) 
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], f"Task '{self.task1.title}' foi apagada com sucesso.")

  