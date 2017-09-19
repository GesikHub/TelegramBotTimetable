import sqlite3
from user import User

class SQLStudents():
    def __init__(self, database):
        self.conection = sqlite3.connect(database)
        self.cursor = self.conection.cursor()

    def insert_students(self, student):
        insert = 'INSERT INTO students (id, first_name, second_name, gruop_number) VALUES (?, ?, ?, ?)'
        self.cursor.execute(insert, (int(student.id), student.name, student.surname, student.number))
        self.conection.commit()

    def select_all(self):
        self.cursor.execute('SELECT * FROM students')
        return self.cursor.fetchall()

    def select_id(self, id):
        self.cursor.execute('SELECT * FROM students WHERE id = ?', (id,))
        return self.cursor.fetchall()[0]

    def counts_row(self):
        self.cursor.execute('SELECT * FROM students')
        result = self.cursor.fetchall()
        return len(result)

    def chek_database(self, id):
        self.cursor.execute('SELECT * FROM students')
        rows = self.cursor.fetchall()
        for student in rows:
            if id in student:
                return True
        return False

    def close(self):
        self.cursor.close()
        self.conection.close()
