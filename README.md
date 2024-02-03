# Password Generator Project

## Overview
This project is a simple password generator web application built with Django and HTML. It allows users to generate random, secure passwords based on their preferences for length, inclusion of numbers, symbols, and uppercase letters.

## Features
- **Customizable Password Length**: Users can specify the length of the generated password.
- **Inclusion Options**: Options to include or exclude numbers, symbols, and uppercase letters.
## Getting Started

### Prerequisites
- Python 3.8 or newer
- Django 3.2 or newer

### Installation

1. Clone the repository:
    ```
    git clone https://github.com/yourusername/password_generator.git
    ```
2. Navigate to the project directory:
    ```
    cd password_generator
    ```
3. Install the required packages:
    ```
    pip install -r requirements.txt
    ```
4. Run the Django migrations to prepare your database:
    ```
    python manage.py migrate
    ```
5. Start the Django development server:
    ```
    python manage.py runserver
    ```
6. Open your web browser and go to `http://127.0.0.1:8000/` to view the application.

## Usage
- Access the web interface via the provided URL.
- Choose your password criteria including length and the inclusion of numbers, symbols, and uppercase letters.
- Click on the "Generate Password" button to generate a password.
