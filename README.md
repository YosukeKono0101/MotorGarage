# MotorGarage

## Overview

MotorGarage is a web application that I developed as part of my course at university and it is designed for an online shopping experience specifically tailored for car parts and accessories. It features various categories like Wheels, Exhaust Systems, and Brakes, with detailed product descriptions and images.

## Features

- **Product Categories**: Users can browse products by categories such as Wheel, Exhaust System, and Brake.
- **Product Details**: Detailed view of each product with descriptions, prices, and images.
- **Search Functionality**: Allows users to search for products based on descriptions.
- **Shopping Cart**: Users can add items to the cart and view them in the shopping cart section.
- **Order Placement**: Users can place orders by filling out a form with their details.
- **Database Sending**: An admin route for seeding the database with initial data.

## Tech Stack

- **Frontend**: HTML, CSS(Bootstrap), JavaScript
- **Backend**: Python with Flask Framework
- **Database**: SQLAlchemy with SQLite
- Flask-WTF for form handling
- Bootstrap for UI components

## Installation and Setup

1. Install the required Python packages: pip install -r requirements.txt
2. Initialize the database with initial seed data: flask run --with-dbseed

## Running the Application

1. Start the Flask server: python run.py
2. Access the application via the web browser at `http://127.0.0.1:5000`.

## Project Structure

- **model.py**: Defines the database models for categories, items, and orders.
- **forms.py**: Contains form definitions for order placement.
- **views.py**: Flask routes for rendering different pages of the application.
- **admin.py**: Admin route for database seeding.
- **templates**: Folder containing HTML templates.
- **static**: Contains static files like images and CSS.

## Usage

- Browse products by categories.
- View detailed information about each product.
- Add products to the shopping cart.
- Place orders by filling out the checkout form.
