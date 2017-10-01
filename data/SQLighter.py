import dj_database_url
import psycopg2
from data.user import User

class SQLStudents():
    def __init__(self, database):
        db_info = dj_database_url.config(default=database)
        self.conection = psycopg2.connect(database=db_info.get('NAME'),
		    		user=db_info.get('USER'),
		    		password=db_info.get('PASSWORD'),
		    		host=db_info.get('HOST'),
		    		port=db_info.get('PORT'))
        self.cursor = self.conection.cursor()

    def insert_students(self, student):
        insert = 'INSERT INTO students (id, first_name, second_name, gruop_number) VALUES (?, ?, ?, ?)'
        self.cursor.execute(insert, (int(student.id), student.name, student.surname, student.number))
        self.conection.commit()

    def create_newtable(self):
        newtable = "CREATE TABLE students (" \
                   "id INTEGER," \
                   "first_name VARCHAR," \
                   "second_name VARCHAR," \
                   "gruop_number VARCHAR," \
                   "PRIMARY KEY (id)" \
                   ")"
        self.cursor.execute(newtable)

    def select_all(self):
        self.cursor.execute('SELECT * FROM students')
        return self.cursor.fetchall()

    def select_id(self, id):
        self.cursor.execute('SELECT * FROM students')
        students = self.cursor.fetchall()
        for student in students:
            if student[0] == id:
                user = User()
                user.student(student[0], student[1], student[2], student[3])
                return user
        return

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
