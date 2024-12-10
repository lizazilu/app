# app
flask app 
{This project is a Flask-based web application that connects to a PostgreSQL database to manage and display a list of courses. The application fetches data from the database and presents it in a user-friendly web interface.}

  1) Features
   
- Connects to a PostgreSQL database hosted on Amazon RDS.
- Fetches and displays course data in a structured HTML table.
- Logs application behavior for debugging and tracking.
  
  2) Technologies Used
- **Backend:** Flask
- **Database:** PostgreSQL
- **Frontend:** HTML with Jinja2 templating
- **Deployment:** Hosted on platform github
  3)  Setup and Installation

** Prerequisites**

- Python (3.9 or later)
- PostgreSQL
- `psycopg2` library for PostgreSQL connection
- Flask library

4)Setup the database:
CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    course_code VARCHAR(20),
    section VARCHAR(10),
    year INT,
    start_date DATE,
    title VARCHAR(100),
    location TEXT,
    credits INT,
    days VARCHAR(10),
    times VARCHAR(50),
    registered INT,
    waitlist INT,
    status VARCHAR(10)
);

INSERT INTO courses (course_code, section, year, start_date, title, location, credits, days, times, registered, waitlist, status)
VALUES 
('ACCT 2025', '1T', 2025, '2025-01-13', 'Managerial Accounting', 'Webster Univ Tashkent, Uzbekistan', 3, 'W', '4:30 PM - 6:50 PM', 24, 0, 'Open'),
('ACCT 2025', '2U', 2025, '2025-01-13', 'Managerial Accounting', 'Webster Univ Tashkent, Uzbekistan', 3, 'F', '4:30 PM - 6:50 PM', 22, 0, 'Open'),
('ACCT 2025', '5U', 2025, '2025-01-13', 'Managerial Accounting', 'Webster Univ Tashkent, Uzbekistan', 3, 'R', '9:00 AM - 11:20 AM', 24, 0, 'Open'),
('ACCT 2025', '8T', 2025, '2025-01-13', 'Managerial Accounting', 'Webster Univ Tashkent, Uzbekistan', 3, 'R', '2:00 PM - 4:20 PM', 24, 0, 'Open');

5) Set environment variables for database connection:

Replace the placeholders with actual values in the code:
DB_HOST = "your-database-endpoint"
DB_NAME = "your-database-name"
DB_USER = "your-username"
DB_PASSWORD = "your-password"
DB_PORT = "your-port"

6) Run the application:

 - python app.py
Author Zlobina Elizaveta- Business Administration & Computer Science student
