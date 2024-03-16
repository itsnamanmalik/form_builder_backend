# Overengineered Form Builder

## Environment variables
Add a `.env` file locally. See `env.example` for the various environment variables you can override/set.

## Running docker compose locally
 * Install Docker
 * Run
```
$ docker compose up
```

This will store the db data under the current directory `./data`.
The server will run on port 80.

If any packages have changed a re-build of the containers may be needed. You can run `docker compose up --build`.

## Autoformatting
Run `poetry run black . --target-version py311` in the root directory.

## Running local commands
Do `docker ps` and then `docker compose exec backend bash`

Once inside you can run `python manage.py createsuperuser` (to create a superuser for example) etc. type django management commands.

## Package management
We use poetry to manage backend packages.

To shows packages that have updates run `poetry show -l`. Update the packages in the pyproject.toml file then to whatever version you would like. Then run `poetry update` to get the updated packages.

