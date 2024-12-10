# app
flask app 
first step was done by creating the database on DBvear with the connected postgreSQL. the connection was done by creating RDS database on aws.


the database sql script:
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


Insert sample course data:
INSERT INTO courses (course_code, section, year, start_date, title, location, credits, days, times, registered, waitlist, status)
VALUES 
('ACCT 2025', '1T', 2025, '2025-01-13', 'Managerial Accounting', 'Webster Univ Tashkent, Uzbekistan', 3, 'W', '4:30 PM - 6:50 PM', 24, 0, 'Open'),
('ACCT 2025', '2U', 2025, '2025-01-13', 'Managerial Accounting', 'Webster Univ Tashkent, Uzbekistan', 3, 'F', '4:30 PM - 6:50 PM', 22, 0, 'Open'),
('ACCT 2025', '5U', 2025, '2025-01-13', 'Managerial Accounting', 'Webster Univ Tashkent, Uzbekistan', 3, 'R', '9:00 AM - 11:20 AM', 24, 0, 'Open'),
('ACCT 2025', '8T', 2025, '2025-01-13', 'Managerial Accounting', 'Webster Univ Tashkent, Uzbekistan', 3, 'R', '2:00 PM - 4:20 PM', 24, 0, 'Open');


then i created the flask on pytcharm :
from flask import Flask, jsonify, render_template
import psycopg2
import logging
creted the index.html in templates
installed libraries to connect database with python code:
pip3 install flask psycopg2-binary



