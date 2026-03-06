#!/bin/bash
set -e

# Run migrations
python manage.py migrate

# Start Gunicorn server
gunicorn config.wsgi:application
