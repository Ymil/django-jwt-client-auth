from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

User = get_user_model()

class JWTBackend(ModelBackend):
    def authenticate(self, request, username=None, **kwargs):
        try:
            user = User.objects.get(username=username)
            return user
        except User.DoesNotExist:
            return None
