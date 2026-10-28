================================================================================
COURSERA BACK-END DEVELOPER CAPSTONE PROJECT: LITTLE LEMON RESTAURANT
PEER REVIEW EVALUATION QUICK GUIDE
================================================================================

Dear Coursera Peer Reviewer,

This project is a fully functional, tested implementation of the Little Lemon 
restaurant backend developed using Python, Django, Django REST Framework, and MySQL.

Below are the exact instructions and endpoints to evaluate each section of the rubric.

--------------------------------------------------------------------------------
1. SETUP & STARTUP INSTRUCTIONS
--------------------------------------------------------------------------------
1. Clone / extract the project folder and navigate into it:
   cd course_Project

2. Activate virtual environment:
   Windows:   .\.venv\Scripts\Activate.ps1   (or create one: python -m venv .venv)
   Linux/Mac: source .venv/bin/activate

3. Install requirements:
   pip install -r requirements.txt

4. Configure Database (.env):
   Create a .env file from .env.example with your MySQL database credentials:
   DB_ENGINE=django.db.backends.mysql
   DB_NAME=littlelemon
   DB_USER=root
   DB_PASSWORD=your_mysql_password
   DB_HOST=127.0.0.1
   DB_PORT=3306

   (Note: If MySQL is not installed in your test environment, set USE_SQLITE=True in .env)

5. Run migrations:
   python manage.py migrate

6. Seed initial test data & create reviewer credentials:
   python manage.py seed_littlelemon
   
   Default Reviewer Credentials created:
   Username: admin
   Password: LittleLemonAdmin2024!
   Reviewer Token: e7ef973b5e250ec174a08265272b9d1e6ff1a381

7. Start the development server:
   python manage.py runserver

8. Run automated tests (27 passing tests):
   python manage.py test

--------------------------------------------------------------------------------
2. WEBSITE PAGES (DJANGO TEMPLATES & STATIC FILES)
--------------------------------------------------------------------------------
Open in your browser:
- Homepage:             http://127.0.0.1:8000/
- Menu Page:            http://127.0.0.1:8000/restaurant/menu-view/
- Table Booking Page:   http://127.0.0.1:8000/restaurant/book/
- Django Admin Site:    http://127.0.0.1:8000/admin/

--------------------------------------------------------------------------------
3. AUTHENTICATION & TOKEN RETRIEVAL
--------------------------------------------------------------------------------
Endpoint: POST http://127.0.0.1:8000/api-token-auth/
Headers:  Content-Type: application/json
Body:
{
  "username": "admin",
  "password": "LittleLemonAdmin2024!"
}

Response (200 OK):
{
  "token": "e7ef973b5e250ec174a08265272b9d1e6ff1a381"
}

User Registration Endpoint:
Endpoint: POST http://127.0.0.1:8000/restaurant/users/  (or /auth/users/)
Body:
{
  "username": "newreviewer",
  "email": "reviewer@coursera.org",
  "password": "Password1234!"
}

--------------------------------------------------------------------------------
4. MENU API ENDPOINTS
--------------------------------------------------------------------------------
A. List All Menu Items:
   Method: GET
   URL:    http://127.0.0.1:8000/restaurant/menu/
   Auth:   None (Public Read)
   Status: 200 OK

B. Create a Menu Item:
   Method: POST
   URL:    http://127.0.0.1:8000/restaurant/menu/
   Auth:   Header: Authorization: Token <your_token>
   Body:
   {
     "title": "Lemon Tart",
     "price": "9.50",
     "inventory": 20
   }
   Status: 201 Created

C. Get Single Menu Item:
   Method: GET
   URL:    http://127.0.0.1:8000/restaurant/menu/1/
   Auth:   None (Public Read)
   Status: 200 OK

D. Update Menu Item:
   Method: PUT
   URL:    http://127.0.0.1:8000/restaurant/menu/1/
   Auth:   Header: Authorization: Token <your_token>
   Body:
   {
     "title": "Greek Salad Deluxe",
     "price": "14.50",
     "inventory": 25
   }
   Status: 200 OK

E. Delete Menu Item:
   Method: DELETE
   URL:    http://127.0.0.1:8000/restaurant/menu/1/
   Auth:   Header: Authorization: Token <your_token>
   Status: 204 No Content

--------------------------------------------------------------------------------
5. TABLE BOOKING API ENDPOINTS
--------------------------------------------------------------------------------
(All Table Booking endpoints require: Header: Authorization: Token <your_token>)

A. List All Bookings:
   Method: GET
   URL:    http://127.0.0.1:8000/restaurant/booking/tables/
   Auth:   Header: Authorization: Token <your_token>
   Status: 200 OK

B. Create a Booking:
   Method: POST
   URL:    http://127.0.0.1:8000/restaurant/booking/tables/
   Auth:   Header: Authorization: Token <your_token>
   Body:
   {
     "name": "Sarah Connor",
     "no_of_guests": 4,
     "booking_date": "2026-11-20",
     "booking_time": "19:00:00",
     "table_number": 4
   }
   Status: 201 Created

C. Get Booking Details:
   Method: GET
   URL:    http://127.0.0.1:8000/restaurant/booking/tables/1/
   Auth:   Header: Authorization: Token <your_token>
   Status: 200 OK

D. Update Booking:
   Method: PUT / PATCH
   URL:    http://127.0.0.1:8000/restaurant/booking/tables/1/
   Auth:   Header: Authorization: Token <your_token>
   Body:
   {
     "no_of_guests": 5
   }
   Status: 200 OK

E. Cancel / Delete Booking:
   Method: DELETE
   URL:    http://127.0.0.1:8000/restaurant/booking/tables/1/
   Auth:   Header: Authorization: Token <your_token>
   Status: 204 No Content

================================================================================
THANK YOU FOR REVIEWING THIS SUBMISSION!
================================================================================
