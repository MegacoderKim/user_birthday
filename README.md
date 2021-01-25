# User Birthdays

## Build

Run `docker-compose build` to build the project

## Run

Run `docker-compose up -d` ro run the project and run `docker-compose logs -f` incase of errors.

### Testing

Run `docker-compose run --rm web py.test` and check the `htmlcov` directory for coverage report

Run `docker-compose run --rm web python manage.py generateapikey` to generate an API key to browse the api

When calling the api clients must pass their API key via the Authorization header. It must be formatted as follows:

```
Authorization: Api-Key ********
```

where **\*\*\*\*** refers to the generated API key
