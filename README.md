# Online Store Inventory and Supplier Management API

This is an API for managing the inventory and suppliers of an online store. It allows employees to add, view, update, and remove items from the inventory, manage suppliers, and establish relationships between items and suppliers.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup](#setup)
  - [Using Virtual Environment](#using-virtual-environment)
  - [Using Docker](#using-docker)
- [Running Tests](#running-tests)
- [API Documentation](#api-documentation)
- [Postman Documentation](#postman-documentation)

## Features

- Inventory Item Management
- Supplier Management
- Item-Supplier Relationship Management
- Secure endpoints using Knox tokens
- API Documentation using Swagger
- Pagination and Filtering of inventory items

## Tech Stack

- Django
- Django REST Framework
- PostgreSQL
- Docker
- Knox for token-based authentication

## Setup

### Using Virtual Environment

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Komatech/online_store_inventory_api.git
    cd online_store_inventory_api
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the PostgreSQL database:**
    - Install PostgreSQL and create a new database and user.
    - Update the env with your database credentials.

5. **Create migrations:**
    ```bash
    python manage.py makemigrations
    ```

6. **Run migrations:**
    ```bash
    python manage.py migrate
    ```

7. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

8. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

### Using Docker

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Komatech/online_store_inventory_api.git
    cd online_store_inventory_api
    ```

2. **Build and run the containers:**
    ```bash
    docker-compose up --build
    ```

## Running Tests

To run the tests, use the following command:

### Using Virtual Environment:
```bash
python manage.py test inventory.test

## API Documentation

The API documentation is generated using Swagger. You can access it at the following URLs once the server is running:

- Swagger UI: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- ReDoc: [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

## Postman Documentation

You can find the Postman documentation for this API at the following URL:

- [Postman Documentation](https://documenter.getpostman.com/view/15533276/2sA3XV9fEo)

