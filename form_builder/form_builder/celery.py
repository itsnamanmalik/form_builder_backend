import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'form_builder.settings')

app = Celery('form_builder')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()