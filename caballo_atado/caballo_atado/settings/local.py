from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "caballo",
        'USER': "postgres",
        'PASSWORD': "alfeinfo",
        'HOST': "localhost",
        'PORT': "5432",
        
    }
}
