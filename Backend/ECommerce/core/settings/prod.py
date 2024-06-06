import config

SECRET_KEY = config.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config.DEBUG

# DB
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config.PG_DB,
        'USER': config.PG_USER,
        'PASSWORD': config.PG_PASSWORD,
        'HOST': config.PG_HOST,
        'PORT': config.PG_PORT,
    }
}