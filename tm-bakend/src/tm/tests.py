import io
from PIL import Image
from rest_framework.test import (APIClient, APITestCase,
                                 URLPatternsTestCase)
from django.contrib.auth import get_user_model
from django.urls import include, path, reverse
from rest_framework_simplejwt.tokens import AccessToken

SIMPLE_JWT = settings.SIMPLE_JWT


class InitClass(APITestCase, URLPatternsTestCase):
    User = get_user_model()

    urlpatterns = [
        path('api/v1/', include('event_crm.urls')),
    ]

    @staticmethod
    def generate_photo_file():
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file

    def create_super_user(self, email='super@test.net'):
        user = get_user_model().objects.get_or_create(email=email,
                                                      password='password',
                                                      is_staff=True,
                                                      is_superuser=True)
        access = AccessToken.for_user(user[0])
        client = self.login_user(access)
        return user[0], client

    @staticmethod
    def login_user(token):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=SIMPLE_JWT['AUTH_HEADER_TYPES'][0] +
                                              ' ' + str(token))  # simulate logged-in user
        return client
