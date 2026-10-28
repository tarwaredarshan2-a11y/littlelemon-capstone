# Little Lemon Restaurant - Coursera Back-End Developer Capstone Project

A complete, production-ready backend implementation of the **Little Lemon** restaurant web application and RESTful API, built with **Django**, **Django REST Framework (DRF)**, and configured for **MySQL**.

---

## 📋 Table of Contents
1. [Project Overview & Tech Stack](#project-overview--tech-stack)
2. [Project Architecture](#project-architecture)
3. [Prerequisites & Installation](#prerequisites--installation)
4. [MySQL Database Setup](#mysql-database-setup)
5. [Environment Configuration (.env)](#environment-configuration-env)
6. [Database Migrations & Sample Data](#database-migrations--sample-data)
7. [Running the Development Server](#running-the-development-server)
8. [Automated Unit Tests](#automated-unit-tests)
9. [API Endpoints Documentation](#api-endpoints-documentation)
10. [Authentication & Registration](#authentication--registration)
11. [Testing with Insomnia / Postman](#testing-with-insomnia--postman)
12. [Troubleshooting](#troubleshooting)

---

## 1. Project Overview & Tech Stack

This project fulfills all requirements of the Meta / Coursera Back-End Developer Capstone:
- **Web Frontend**: Server-rendered HTML templates for Little Lemon homepage, menu, and table booking with custom CSS styling and responsive layout.
- **Menu API**: Complete CRUD endpoints for menu items with serialization, permissions, and validation.
- **Table Booking API**: Complete CRUD endpoints for restaurant reservations with guest limit validations and unique booking reference generation.
- **Authentication**: Token-based authentication using Django REST Framework and Djoser, with public read permissions for menus and token-protected booking operations.
- **Primary Database**: MySQL integration via `pymysql` with environment-based configuration and SQLite fallback for test environments.
- **Unit Testing**: Automated test suite testing models, serializers, views, permissions, and auth workflows.

### Technologies Used
- **Python 3**
- **Django 6.x**
- **Django REST Framework (DRF)**
- **Djoser** (User registration & token management)
- **PyMySQL** (Pure-Python MySQL driver)
- **python-dotenv** (Environment variable management)
- **HTML5 & CSS3**

---

## 2. Project Architecture

```
course_Project/
├── littlelemon/               # Project configuration package
│   ├── __init__.py            # PyMySQL MySQLdb installation hook
│   ├── asgi.py
│   ├── settings.py            # Settings with MySQL & DRF configuration
│   ├── urls.py                # Root URL routing & Auth endpoints
│   └── wsgi.py
├── restaurant/                # Core restaurant application
│   ├── admin.py               # Django Admin model registrations
│   ├── apps.py
│   ├── fixtures/
│   │   └── sample_data.json   # Optional initial database fixture
│   ├── management/
│   │   └── commands/
│   │       └── seed_littlelemon.py # Database seeding command
│   ├── migrations/            # Django database migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py              # MenuItem and Booking models
│   ├── serializers.py         # DRF serializers & field validators
│   ├── urls.py                # Restaurant application routes
│   └── views.py               # HTML template views & DRF API viewsets
├── static/
│   └── css/
│       └── style.css          # Little Lemon branding stylesheet
├── templates/
│   ├── base.html              # Base HTML layout
│   ├── index.html             # Homepage
│   ├── menu.html              # Dynamic menu page
│   └── book.html              # Table booking reservation page
├── tests/                     # Automated test suite
│   ├── __init__.py
│   ├── test_models.py         # Model & string representation tests
│   ├── test_serializers.py    # Serializer validation tests
│   └── test_views.py          # API endpoint & auth tests
├── .env.example               # Environment variables template
├── .gitignore                 # Git ignore rules
├── manage.py                  # Django administrative script
├── README.md                  # Comprehensive documentation
├── Readme.txt                 # Quick reference for Coursera peer reviewers
└── requirements.txt           # Project dependencies
```

---

## 3. Prerequisites & Installation

### Prerequisites
- Python 3.10+ (tested up to Python 3.14)
- MySQL Server 8.x (or MariaDB)
- Git

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd course_Project
   ```

2. **Create and activate a virtual environment:**
   - On Windows (PowerShell):
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
   - On Linux / macOS:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 4. MySQL Database Setup

1. Open your MySQL client (Command Line, MySQL Workbench, or phpMyAdmin) as root or an administrative user:
   ```bash
   mysql -u root -p
   ```

2. Execute the following SQL commands to create the database:
   ```sql
   CREATE DATABASE littlelemon CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```

3. (Optional) Create a dedicated user for the application:
   ```sql
   CREATE USER 'littlelemon_user'@'localhost' IDENTIFIED BY 'littlelemon_password';
   GRANT ALL PRIVILEGES ON littlelemon.* TO 'littlelemon_user'@'localhost';
   FLUSH PRIVILEGES;
   ```

---

## 5. Environment Configuration (.env)

Copy `.env.example` to `.env`:
```bash
cp .env.example .env     # Linux / macOS
copy .env.example .env   # Windows
```

Edit `.env` to match your MySQL server credentials:
```ini
SECRET_KEY=django-insecure-littlelemon-capstone-change-in-production-12345
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# MySQL Database Settings
DB_ENGINE=django.db.backends.mysql
DB_NAME=littlelemon
DB_USER=root
DB_PASSWORD=your_actual_mysql_password
DB_HOST=127.0.0.1
DB_PORT=3306

# SQLite fallback (Set to True only if MySQL server is unavailable)
USE_SQLITE=False
```

---

## 6. Database Migrations & Sample Data

1. **Apply migrations to create the MySQL schema:**
   ```bash
   python manage.py migrate
   ```

2. **Seed sample data and create the default admin user:**
   ```bash
   python manage.py seed_littlelemon
   ```
   This will automatically create:
   - Default superuser: `admin` / `LittleLemonAdmin2024!`
   - An active API Authentication Token for `admin`
   - Initial menu items (Greek Salad, Bruschetta, Lemon Dessert, Grilled Fish, Pasta Alfredo, Mediterranean Pizza)
   - A sample table reservation

*(Alternatively, you can load the fixture with: `python manage.py loaddata restaurant/fixtures/sample_data.json`)*.

---

## 7. Running the Development Server

Start the Django local server:
```bash
python manage.py runserver
```

Open your browser:
- **Homepage**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/) or [http://127.0.0.1:8000/restaurant/](http://127.0.0.1:8000/restaurant/)
- **Menu Webpage**: [http://127.0.0.1:8000/restaurant/menu-view/](http://127.0.0.1:8000/restaurant/menu-view/)
- **Table Booking Webpage**: [http://127.0.0.1:8000/restaurant/book/](http://127.0.0.1:8000/restaurant/book/)
- **Django Admin**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 8. Automated Unit Tests

Run the complete automated test suite (27 unit tests):
```bash
python manage.py test
```

Or run tests specifically for the restaurant app:
```bash
python manage.py test restaurant
```

The test suite covers:
- **Models**: String formatting, decimal handling, auto-generated booking references.
- **Serializers**: Validation for price (> 0), inventory (>= 0), guest limits (1-20), non-empty names.
- **Menu API**: Unauthenticated public GET, authenticated POST, single item GET, PUT, PATCH, DELETE.
- **Booking API**: Unauthenticated permission denial (401), authenticated CRUD operations.
- **Auth**: User registration, token acquisition, and authenticated token requests.
- **Templates**: HTTP 200 checks and template assertion for web pages.

---

## 9. API Endpoints Documentation

### Menu API

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| `GET` | `/restaurant/menu/` | List all menu items | No |
| `POST` | `/restaurant/menu/` | Create a new menu item | **Yes** (Token) |
| `GET` | `/restaurant/menu/<id>/` | Retrieve a single menu item | No |
| `PUT` | `/restaurant/menu/<id>/` | Full update of a menu item | **Yes** (Token) |
| `PATCH` | `/restaurant/menu/<id>/` | Partial update of a menu item | **Yes** (Token) |
| `DELETE` | `/restaurant/menu/<id>/` | Delete a menu item | **Yes** (Token) |

#### Example Request Body for `POST /restaurant/menu/`:
```json
{
  "title": "Grilled Salmon",
  "price": "22.50",
  "inventory": 15
}
```

---

### Table Booking API

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| `GET` | `/restaurant/booking/tables/` | List all table bookings | **Yes** (Token) |
| `POST` | `/restaurant/booking/tables/` | Create a new table reservation | **Yes** (Token) |
| `GET` | `/restaurant/booking/tables/<id>/` | Retrieve a reservation by ID | **Yes** (Token) |
| `PUT` | `/restaurant/booking/tables/<id>/` | Update a reservation | **Yes** (Token) |
| `PATCH` | `/restaurant/booking/tables/<id>/` | Partially update a reservation | **Yes** (Token) |
| `DELETE` | `/restaurant/booking/tables/<id>/` | Cancel / delete a reservation | **Yes** (Token) |

#### Example Request Body for `POST /restaurant/booking/tables/`:
```json
{
  "name": "Jane Doe",
  "no_of_guests": 4,
  "booking_date": "2026-11-25",
  "booking_time": "19:30:00",
  "table_number": 5
}
```

---

### Authentication & User Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api-token-auth/` | Obtain auth token (Django REST Framework) |
| `POST` | `/auth/token/login/` | Obtain auth token (Djoser) |
| `POST` | `/auth/token/logout/` | Logout / destroy auth token (Djoser) |
| `POST` | `/restaurant/users/` | Register a new user |
| `POST` | `/auth/users/` | Register a new user (Djoser) |

---

## 10. Authentication & Registration

### 1. Registering a User
Send a `POST` to `/restaurant/users/` (or `/auth/users/`):
```json
{
  "username": "reviewer1",
  "email": "reviewer1@example.com",
  "password": "SecurePassword123!"
}
```

### 2. Obtaining a Token
Send a `POST` to `/api-token-auth/`:
```json
{
  "username": "reviewer1",
  "password": "SecurePassword123!"
}
```
**Response:**
```json
{
  "token": "e7ef973b5e250ec174a08265272b9d1e6ff1a381"
}
```

### 3. Making Authenticated Requests
In Insomnia, Postman, or cURL, add the `Authorization` header:
```
Authorization: Token <your_token_here>
```

---

## 11. Testing with Insomnia / Postman

1. **Test Public Menu List**:
   - `GET http://127.0.0.1:8000/restaurant/menu/`
   - No headers needed. Status: `200 OK`.

2. **Obtain Token**:
   - `POST http://127.0.0.1:8000/api-token-auth/`
   - Body (JSON): `{"username": "admin", "password": "LittleLemonAdmin2024!"}`
   - Status: `200 OK`. Copy the returned `token`.

3. **Test Protected Table Booking List**:
   - `GET http://127.0.0.1:8000/restaurant/booking/tables/`
   - Header: `Authorization: Token <your_copied_token>`
   - Status: `200 OK`.

4. **Create a Reservation**:
   - `POST http://127.0.0.1:8000/restaurant/booking/tables/`
   - Header: `Authorization: Token <your_copied_token>`
   - Body (JSON):
     ```json
     {
       "name": "Maria Garcia",
       "no_of_guests": 2,
       "booking_date": "2026-11-28",
       "booking_time": "20:00:00",
       "table_number": 3
     }
     ```
   - Status: `201 Created`.

---

## 12. Troubleshooting

- **Error: Can't connect to MySQL server on '127.0.0.1' (10061)**:
  Make sure your MySQL service is started (e.g. `net start MySQL80` or `sudo systemctl start mysql`). If you are running in an environment without MySQL installed, you can temporarily set `USE_SQLITE=True` in your `.env` to execute migrations and tests locally.
- **Error: Access denied for user 'root'@'localhost'**:
  Verify your MySQL password in `.env`.
- **401 Unauthorized**:
  Ensure you included the word `Token ` before your token key in the `Authorization` header (`Authorization: Token <token>`).
