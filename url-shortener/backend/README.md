# URL Shortener Backend

This is the backend for the URL Shortener application built using Django and Django REST Framework. The backend is responsible for handling URL shortening requests, managing the database, and providing a RESTful API for the frontend.

## Project Structure

- **manage.py**: Command-line utility for managing the Django project.
- **pyproject.toml**: Configuration file for Poetry, specifying project dependencies and settings.
- **url_shortener/**: Contains the main Django project files.
  - **settings.py**: Django settings for the project.
  - **urls.py**: URL routing for the Django application.
  - **wsgi.py**: Entry point for WSGI-compatible web servers.
- **shortener/**: Contains the URL shortener application files.
  - **models.py**: Data models for the URL shortener application.
  - **serializers.py**: Serializers for converting model instances to JSON format.
  - **views.py**: Views for handling HTTP requests and responses.
  - **urls.py**: URL routing specific to the shortener app.
  - **tests.py**: Test cases for the shortener application.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Poetry for dependency management
- Docker and Docker Compose for containerization

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd url-shortener/backend
   ```

2. Install dependencies using Poetry:
   ```
   poetry install
   ```

### Running the Application

To run the backend application, you can use Docker. Make sure you have Docker and Docker Compose installed, then run:

```
docker-compose up
```

This command will build the Docker images and start the backend service.

### API Endpoints

The backend provides the following API endpoints:

- `POST /shorten/`: Shorten a given URL.
- `GET /shorten/<shortened_id>/`: Retrieve the original URL for a given shortened ID.

### Running Tests

To run the tests for the backend application, use the following command:

```
pytest
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.