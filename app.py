from flask import Flask, jsonify, render_template
import psycopg2
import logging
import os


app = Flask(__name__)

# Logging Configuration
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Database Configuration
DB_HOST = "db-sb2.c1oqycm043tr.us-east-1.rds.amazonaws.com"
DB_NAME = "lizadb"
DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_PORT = "5432"

# Connect to the Database
def get_db_connection():
    try:
        logging.debug("Attempting to connect to the database...")
        connection = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        logging.debug("Database connection established.")
        return connection
    except Exception as e:
        logging.error(f"Error connecting to database: {e}")
        return None

# Root Route (Landing Page)
@app.route('/')
def home():
    logging.debug("Home route accessed.")
    return "<h1>Welcome to the Flask Application</h1><p>Visit <a href='/courses'>/courses</a> to see the courses.</p>"

# Route to fetch courses
@app.route('/courses', methods=['GET'])
def get_courses():
    logging.debug("Fetching courses from the database.")
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            logging.debug("Executing SQL query: SELECT * FROM courses")
            cursor.execute("SELECT * FROM courses")

            courses = cursor.fetchall()
            logging.debug(f"Courses fetched successfully: {courses}")
            cursor.close()
            connection.close()
            return render_template('templates/index.html', courses=courses)
        except Exception as e:
            logging.error(f"Error fetching courses: {e}")
            return f"Error fetching courses: {e}", 500
    else:
        logging.error("Failed to connect to the database.")
        return "Could not connect to the database.", 500

if __name__ == '__main__':
    logging.info("Starting the Flask application...")
    app.run(host='0.0.0.0', port=5000, debug=True)






