import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'creditkelin.settings.prod')
django.setup()

User = get_user_model()

SUPERUSER_EMAIL = 'admin@example.com'
SUPERUSER_USERNAME = 'admin'
SUPERUSER_PASSWORD = '1234'  

if not User.objects.filter(username=SUPERUSER_USERNAME).exists():
    User.objects.create_superuser(
        username=SUPERUSER_USERNAME,
        email=SUPERUSER_EMAIL,
        password=SUPERUSER_PASSWORD
    )
    print('Superuser created.')
else:
    print('Superuser already exists.')
