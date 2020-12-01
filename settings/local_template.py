from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
# Use for example the command line command below to generatea a secret key
# $ python  -c 'from django.core.management import utils; print(utils.get_random_secret_key())'
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # Locate the database in a 'database' directory *outside* the
        # project directory. The 'database' directory needs to be
        # created first by the user.
        'NAME': BASE_DIR / '..' / 'database' / 'db.sqlite3',
    }
}
