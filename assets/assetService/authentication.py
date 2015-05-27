from rest_framework import authentication
from django.contrib.auth.models import User


class NoAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        return User.objects.all()[0], ''