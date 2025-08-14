# URL Shortener Project

This project is a URL shortener application built using Django and Django REST Framework for the backend, and React for the frontend. The application allows users to shorten long URLs and retrieve them easily.

## Project Structure

The project is organized into two main directories: `backend` and `frontend`.

### Backend

The backend is built with Django and includes the following components:

- **manage.py**: Command-line utility for managing the Django project.
- **pyproject.toml**: Configuration file for Poetry, specifying project dependencies and settings.
- **url_shortener/**: Main Django application directory containing:
  - **settings.py**: Django settings, including database configuration and installed apps.
  - **urls.py**: URL routing for the Django application.
  - **wsgi.py**: Entry point for WSGI-compatible web servers.
- **shortener/**: Django app for URL shortening, containing:
  - **models.py**: Data models for the URL shortener application.
  - **serializers.py**: Serializers for converting model instances to JSON.
  - **views.py**: Views for handling HTTP requests and responses.
  - **urls.py**: URL routing specific to the shortener app.
  - **tests.py**: Test cases for the shortener application.

### Frontend

The frontend is built with React and includes the following components:

- **package.json**: Configuration file for npm, listing dependencies and scripts.
- **public/index.html**: Main HTML file for the React application.
- **src/**: Source directory containing:
  - **App.js**: Main App component for the React application.
  - **index.js**: Entry point for the React application.
  - **components/UrlShortener.js**: Component for handling the user interface for shortening URLs.

### Docker

The project is containerized using Docker, with the following files:

- **docker-compose.yml**: Defines services, networks, and volumes for running the backend and frontend together.
- **Dockerfile.backend**: Instructions for building the Docker image for the backend service.
- **Dockerfile.frontend**: Instructions for building the Docker image for the frontend service.

## Getting Started

To run the application, ensure you have Docker and Docker Compose installed. Then, use the following command to build and run the application:

```bash
docker-compose up --build
```

This command will start both the backend and frontend services, allowing you to access the URL shortener application in your web browser.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.