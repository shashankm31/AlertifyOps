# AlertifyOps - Backend Setup

## Objective

The Objective of this phase is to build the backend foundation for AlertifyOps.

This includes:

- FastAPI application setup
- Database configuration
- SQLAlchemy ORM integration
- Request and Response validation
- CRUD REST APIs

This backend will later be containerized using Docker and deployed to Kubernetes.

# Project Structure










# Folder Explanation

## api/

Contains all REST API endpoints

Example:

- POST /alerts
- GET /alerts
- PUT /alerts/{id}
- DELETE /alerts/{id}

Each endpoint received HTTP requests and returns HTTP responses.

-----

## database/

Responsible for database connectivity.

Contains:

- Database Engine
- SessionLocal
- Base
- get_db()

This module creates database sessions that are used by API routes.

-----

## models/

Defines SQLAlchemy models that represent database tables.

Each model represents one database table.

Current model:

Alert 

The Alert model represents the alerts table inside the database.

Each object created from the Alert model corresponds to one database row.

Example:





-----

## schemas/

Defines Pydantic models used for request validation and response serialization.

Schemas validate incoming request data and format outgoing responses.

They do not create database tables.

Current schemas:

AlertCreate

Used for validating incoming request payloads.

AlertResponse

Used for formatting API responses.

Schemas are responsible only for data validation and serialization.

They do not create database tables.

-----

## services/

Contains business logic and application processing, keeping API routes clean and maintainable.

Currently empty.

later it will contain:

 - Alert validation
 - Duplicate detection
 - Incident generation

This keeps API routes clean.


## main.py

Entry point of the FastAPI application.

Responsibilities:

- Create FastAPI application
- Register API routers
- Create database tables
- Start the backend server

-----

# Backend Request Flow











# Current Features

- FastAPI Application
- SQLite Database
- SQLAlchemy ORM
- CRUD APIs
- Swagger UI

-----

# Future Enhancements

- PostgreSQL
- JWT Authentication
- Docker
- Kubernetes
- Github Actions
- Terraform
- AWS