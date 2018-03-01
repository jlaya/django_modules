#!/bin/bash
cd /home/ubuntu/env/
source entorno/bin/activate
cd /home/ubuntu/atx/
python3 manage.py runserver 0.0.0.0:80


