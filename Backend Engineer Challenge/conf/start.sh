#!/bin/bash

set -e

python /app/manage.py migrate

if [[ "$(tr [:upper:] [:lower:] <<< ${DEBUG})" == "true" ]]; then
    echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(email='admin@example.com').delete(); User.objects.create_superuser('admin', 'admin@example.com', 'root')" | python manage.py shell
    python /app/manage.py runserver_plus 0:8000
else
    supervisord -n -c /etc/supervisor/supervisord.conf
fi
