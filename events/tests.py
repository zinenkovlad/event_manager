from datetime import datetime

from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Event


class EventTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@email.com",
            password="secret"
        )

        self.event = Event.objects.create(
            title="Test event",
            description="Test event description",
            organizer=self.user,
            location="Test location",
            date=datetime.now()
        )

    def test_event_model(self):
        self.assertEqual(self.event.organizer.username, "testuser")
        self.assertEqual(self.event.title, "Test event")

    def test_event_registration(self):
        self.client.force_login(self.user)
        url = reverse('event_registration', kwargs={'pk': self.event.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(self.event.attendees.filter(pk=self.user.pk).exists())
