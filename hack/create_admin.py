import os
from django.contrib.auth import get_user_model
User = get_user_model()

username = os.getenv('USER','aymen')
email = os.getenv('EMAIL','ay28mene@gmail.com')
password = os.getenv('PASSWORD','aymen')
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print("Superuser created")
else:
    print("Superuser already exists")
