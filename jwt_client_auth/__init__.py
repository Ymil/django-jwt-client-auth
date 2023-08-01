__version__ = '0.1.0'

from django.conf import settings

JWT_ENDPOINT = getattr(settings, 'JWT_ENDPOINT')
JWT_REDIRECT_URL = getattr(settings, 'JWT_REDIRECT_URL', 'login_ok')
JWT_ENDPOINT_SSL_VERIFY = getattr(settings, 'JWT_ENDPOINT_SSL_VERIFY', True)
JWT_ENDPOINT_ERROR_MESSAGE_FIELD = getattr(settings, 'JWT_ENDPOINT_ERROR_MESSAGE', 'message')