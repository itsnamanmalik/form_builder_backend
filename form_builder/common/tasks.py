import string

from account.models import Account
from django.utils.crypto import get_random_string

from celery import shared_task

@shared_task
def create_random_user_accounts(total):
    """
    Create random user accounts
    """
    for _ in range(total):
        username = 'user_{}'.format(get_random_string(10, string.ascii_letters))
        email = '{}@example.com'.format(username)
        password = get_random_string(50)
        Account.objects.create_user(email=email, password=password)
    return '{} random users created with success!'.format(total)
