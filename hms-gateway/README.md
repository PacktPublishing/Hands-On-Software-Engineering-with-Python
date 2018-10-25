# HMS Artisan Gateway

Provides an executable service that the Artisan Application and Central 
Office Application use to send information back and forth between the 
artisans and the central office.

## Python Virtual Environment

**Create:** `python3 -m venv ~/py_envs/hms/gateway`
**Activate:** `source ~/py_envs/hms/gateway/bin/activate`
**Upgrade pip:** `pip install --upgrade pip`

## Build process

`python3 setup.py sdist` (source-distribution)
