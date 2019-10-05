#!/bin/bash
# set -e : força o script a sair caso qqr erro ocorra
set -e

cd django_crud

python manage.py migrate

python manage.py runserver 0.0.0.0:8000
