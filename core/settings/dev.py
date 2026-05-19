from .base import env

# Override base settings for local development
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Connect to your Neon DB securely via your existing .env file
DATABASES = {
    'default': env.db('DATABASE_URL')
}
