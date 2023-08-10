__version__ = '0.1.0'

from django.conf import settings

try:
    JWT_ENDPOINT = getattr(settings, 'JWT_ENDPOINT')
except AttributeError:
    raise Exception('JWT_ENDPOINT must be defined in settings.py')

JWT_REDIRECT_URL = getattr(settings, 'JWT_REDIRECT_URL', 'login_ok')
JWT_ENDPOINT_SSL_VERIFY = bool(getattr(settings, 'JWT_ENDPOINT_SSL_VERIFY', True))
JWT_ENDPOINT_ERROR_MESSAGE_FIELD = getattr(settings, 'JWT_ENDPOINT_ERROR_MESSAGE', 'message')