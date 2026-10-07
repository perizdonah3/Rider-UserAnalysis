from os import name

from django.test import TestCase
from django.shortcuts import reverse
from .models import *
from django.http import HttpResponse

class AppointmentModelTest(TestCase):
    def test_create_appointment(self):
        appointment=Appointment.objects.create(
        name="",
        email="",
        phone="",
        date="",
        time="",
        notes="",
        )
        self.assertEqual(str(appointment),"")
        self.assertEqual(Appointment.objects.count(),"")


class ContactMessageModelTest(TestCase):
    def test_create_contact_message(self):
        msg=ContactMessage.objects.create(
            name="",
            email="",
            message="",
        )
        self.assertEqual(str(msg),"")
        self.assertEqual(ContactMessage.objects.count(),)


class ViewsTest(TestCase):
    def test_home_page_loads(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_loads(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_contact_page_loads(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)



# Create your tests here.
