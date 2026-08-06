# Database Architecture

## Overview

The Database layer is responsible for storing, retrieving, updating and deleting application data.

AlertifyOps uses SQLAlchemy ORM to communicate with the database instead of writing raw SQL queries.

During development, SQLite is used because it is lightweight and requires minimal configuration.

The application will later migrate to PostgreSQL for production deployment.

-----

# Why do we Need a Database?

A backend application must persist data.

Without a database, all information would be lost whenever the application restarts.

Example

Incoming Alert

Device : RTR-01
Status: DOWN
