from .base import *

# ######### DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG
# ######### END DEBUG CONFIGURATION


# ######### EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# ######### END EMAIL CONFIGURATION
