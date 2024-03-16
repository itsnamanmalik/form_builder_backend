# Overengineered Form Builder
Welcome to Overengineered Form Builder, an excessively complex yet fascinating project aimed at developing a form builder application where users can create custom forms with various field types. Users can fill out these forms, and form administrators can access and analyze the form entries.

## Introduction
Overengineered Form Builder is not just another form builder application; it's a showcase of the extensive use of backend tools and technologies. This project aims to demonstrate how various backend technologies can be integrated to create a robust and scalable form builder solution.

## Features
- **Custom Form Creation**: Users can create custom forms by adding various field types such as text, multi-select, dropdown, file upload, etc.
- **Dynamic Form Rendering**: The forms are dynamically rendered based on the configuration set by the user.
- **User Authentication**: Secure user authentication and authorization mechanisms ensure that only authorized users can access and manage forms.
- **Form Submission Handling**: Efficient handling of form submissions with proper validation and storage mechanisms.
- **Admin Dashboard**: Administrators have access to a comprehensive dashboard where they can view form entries, analyze data, and manage forms.
- **Extensive Backend Tools**: The project utilizes a plethora of backend tools and technologies, making it a prime example of overengineering.
  
## Technologies Used
- **Backend**: Django
- **Database**: PostgreSQL
- **Authentication**: JWT (JSON Web Tokens)
- **Frontend**: React.js
- **State Management**: Redux
- **Styling**: CSS-in-JS (Styled Components)
- **Distributed Task Queue**: Celery with RabbitMQ
- **Caching**: Redis
- **Containerization**: Docker
- with more to come...


## Getting Started

### Environment variables
Add a `.env` file locally. See `env.example` for the various environment variables you can override/set.

### Running docker compose locally
 * Install Docker
 * Run
```
$ docker compose up
```

This will store the db data under the current directory `./data`.
The server will run on port 80.

If any packages have changed a re-build of the containers may be needed. You can run `docker compose up --build`.

### Autoformatting
Run `poetry run black . --target-version py311` in the root directory.

### Running local commands
Do `docker ps` and then `docker compose exec backend bash`

Once inside you can run `python manage.py createsuperuser` (to create a superuser for example) etc. type django management commands.

### Package management
We use poetry to manage backend packages.

To shows packages that have updates run `poetry show -l`. Update the packages in the pyproject.toml file then to whatever version you would like. Then run `poetry update` to get the updated packages.

