## Blockr-mock
This repository contains a mock server for the Sidechains en Smartcontracts repository.

### Development
 - First install make if you don't have this already
 - Run `make dev`
 - Run 'docker-compose run --rm backend python manage.py createsuperuser' and fill in the details
 - Run `make fake` to insert some fake data within

### Formatting
 - `make black` will format the whole project to the black rules
 - `make flake8` will check the code against flake8 code conventions
