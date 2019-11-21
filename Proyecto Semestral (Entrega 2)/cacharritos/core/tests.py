from django.test import TestCase,Client
from django.contrib.auth.models import User  ## usuario
from .forms import CustomUserForm
from django.urls import reverse


# Create your tests here.


class gestion_Usuario(TestCase):
    def setUp (self):
        self.cliente = Client()
        User.objects.create_user('Li',password= 'adminadmin')
    


    def test_Login(self):
        response= self.cliente.post(
            reverse('login'),{'username':'Li','password':'adminadmin'})
        self.assertEqual(response.status_code,302,'prueba exitosa')



    def test_Login_Fail(self):
        response= self.cliente.post(
            reverse('login'),{'username':'Li','password':'admin'})
        self.assertNotEqual(response.status_code,302,'prueba exitosa')    

