# Choreo Backend Test

A simple FastAPI-based backend application for testing and health check monitoring.

## Overview

This is a minimal FastAPI backend service that provides health status endpoints. It demonstrates a clean project structure with separate routes and services layers.

## Project Structure

```
choreo-be-test/
├── main.py              # FastAPI application entry point
├── requirements.txt     # Python dependencies
├── app/
│   ├── routes/
│   │   └── router.py    # API route definitions
│   └── services/
│       └── healthService.py  # Business logic for health checks
└── README.md           # This file
```

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd choreo-be-test
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
```

3. Activate the virtual environment:
   - On Linux/macOS:
   ```bash
   source venv/bin/activate
   ```
   - On Windows:
   ```bash
   venv\Scripts\activate
   ```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the server using Uvicorn:

```bash
uvicorn main:app --reload
```

The `--reload` flag enables auto-restart when code changes are detected. This is useful during development.

By default, the application runs on `http://localhost:8000`

### Interactive API Documentation

Once the server is running, you can access:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### Health Check

**Endpoint**: `GET /health-check`

**Description**: Returns the health status of the application.

**Query Parameters**:
- `status` (optional, string): Set to `'good'` for healthy status, any other value for degraded status
  - Default: `'good'`

**Request Examples**:

```bash
# Check healthy status
curl http://localhost:8000/health-check

# Check degraded status
curl http://localhost:8000/health-check?status=bad
```

**Response Examples**:

Success (status='good'):
```json
{
  "health": "Healthy"
}
```

Degraded (status != 'good'):
```json
{
  "health": "Oh oh, I am not doing well"
}
```

## Dependencies

This project uses the following key dependencies:

- **FastAPI**: Modern, fast web framework for building APIs
- **Uvicorn**: ASGI web server
- **Pydantic**: Data validation using Python type annotations
- **Python-dotenv**: Environment variable management

For a complete list of dependencies, see `requirements.txt`

## Development

### Directory Layout Explanation

- **main.py**: Contains the FastAPI application instance and router registration
- **app/routes/router.py**: Defines all API endpoints and their handlers
- **app/services/healthService.py**: Contains business logic for the health check functionality

This separation follows a common pattern where routes handle HTTP concerns and services contain the actual business logic.

## Future Enhancements

- Add database integration
- Add authentication and authorization
- Add more comprehensive health checks
- Add logging and monitoring
- Add unit and integration tests
- Add Docker support

## License

This project is a test repository. See LICENSE file for details (if applicable).
