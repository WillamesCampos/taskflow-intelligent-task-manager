# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/
from taskflow.config.settings.base import BASE_DIR


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

