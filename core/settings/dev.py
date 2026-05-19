from .base import *

# Override base settings for local development
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Intercept the FastAPI async URL and convert it to Django's sync format
db_url = env('DATABASE_URL').replace('postgresql+asyncpg', 'postgres')

DATABASES = {
    'default': environ.Env.db_url_config(db_url)
}
