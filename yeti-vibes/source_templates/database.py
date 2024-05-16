# save gestures for each camera in the database (postgre-sql)

import psycopg2

class Database:
    def __init__(self):
        # Connect to PostgreSQL database
        self.conn = psycopg2.connect("dbname='your_database' user='your_user' host='localhost' password='your_password'")
        self.cursor = self.conn.cursor()

    def save_gesture(self, gesture, camera_id):
        # Save detected gesture and associated camera ID to the database
        query = "INSERT INTO gestures (gesture, camera_id) VALUES (%s, %s)"
        self.cursor.execute(query, (gesture, camera_id))
        self.conn.commit()