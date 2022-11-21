# Створіть за допомогою класів та продемонструйте свою реалізацію шкільної бібліотеки (включіть фантазію).
# Наприклад вона може містити класи Person, Teacher, Student, Book, Shelf, Author, Category і.т.д. Можна робити по
# прикладу банкомату з меню, базою даних і т.д.


import sqlite3
from datetime import datetime


class Person(object):

    def __init__(self, name, status):
        self.name = name
        self.status = status

    def book_history(self):
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM LOG WHERE NAME=?''', (self.name, ))
        history = cursor.fetchall()
        print('You already read:')
        books = []
        for line in history:
            books.append(line[3])
        books = set(books)
        for book in books:
            print(f'<{book}>')


class Student(Person):

    def student_books(self):
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT NAME FROM BOOKS WHERE LOCATION=?''', (self.name, ))
        books = cursor.fetchall()
        if len(books) == 0:
            print('You have not any book!')
        else:
            print('You have next books:')
            for line in books:
                print(line[0])

    def take_book(self):
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM BOOKS WHERE AVAILABLE="TRUE"''')
        books = cursor.fetchall()
        print('Available books for reading:')
        for line in books:
            print(f'[{books.index(line) + 1}] <{line[1]}> by {line[2]} written in {line[3]}')
        choose = int(input('Please enter the number of book to take ->'))
        book_name = books[choose - 1][1]
        print(book_name)
        cursor = conn.cursor()
        cursor.execute('''UPDATE BOOKS SET AVAILABLE=? WHERE NAME=?''', ("FALSE", book_name,))
        cursor.execute('''UPDATE BOOKS SET LOCATION=? WHERE NAME=?''', (self.name, book_name,))
        conn.commit()
        log(self.name, book_name, "FALSE")
        print(f'Please take your: <{books[choose - 1][1]}>')

    def return_book(self):
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM BOOKS WHERE LOCATION=?''', (self.name, ))
        books = cursor.fetchall()
        print('You have next registered books:')
        for line in books:
            print(f'[{books.index(line) + 1}] <{line[1]}> by {line[2]} written in {line[3]}')
        choose = int(input('Please enter the number of book to return ->'))
        book_name = books[choose - 1][1]
        cursor = conn.cursor()
        cursor.execute('''UPDATE BOOKS SET AVAILABLE=? WHERE NAME=?''', ("TRUE", book_name,))
        cursor.execute('''UPDATE BOOKS SET LOCATION=? WHERE NAME=?''', ("Shelf 1", book_name,))
        conn.commit()
        log(self.name, book_name, "TRUE")
        print(f'Please take your: <{books[choose - 1][1]}> on the Shelf 1')


def log(name, book, rtn):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    tm = datetime.now()
    cursor.execute('''INSERT INTO LOG (NAME, TIME, BOOK, RETURN) VALUES(?, ?, ?, ?)''',
                    (name, tm, book, rtn))
    conn.commit()
    conn.close()


class Teacher(Person):

    @staticmethod
    def create_student(name, password, st_class):
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT NAME FROM USERS''')
        names = cursor.fetchall()
        name_list = []
        for nm in names:
            name_list.append(nm[0])
        if name not in name_list:
            cursor.execute('''INSERT INTO USERS (NAME, PASSWORD, STATUS, CLASS) VALUES(?, ?, ?, ?)''',
                           (name, password, 'Student', st_class))
        conn.commit()
        print(f'The student {name} created!')

    @staticmethod
    def add_book(name, year, author, location):
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO BOOKS (NAME, AUTHOR, YEAR, LOCATION, AVAILABLE) VALUES(?, ?, ?, ?, ?)''',
                           (name, year, author, location, 'TRUE'))
        conn.commit()
        print(f'The book {name} is on the shelf!')


def menu():
    print('|| Login as Student: enter "1" || Login as Teacher: enter  "2" || Exit: enter "0" ||')
    try:
        command = int(input('Please enter the command:'))
        return command
    except ValueError:
        print("Please enter correct menu number!")


def student_menu():
    print('|| Check my books: enter "1" || Take a book: enter "2" || Return a book: enter "3" || '
          'Check book history: enter "4" || Exit: enter "0" ||')
    try:
        command = int(input('Please enter the command:'))
        return command
    except ValueError:
        print("Please enter correct menu number!")


def student_workflow(active_student):
    active = True
    while active:
        command = student_menu()
        if command == 1:
            active_student.student_books()
        elif command == 2:
            active_student.take_book()
        elif command == 3:
            active_student.return_book()
        elif command == 4:
            active_student.book_history()
        elif command == 0:
            print("Session finished!")
            active = False
        else:
            print('Please enter correct menu number!')


def teacher_menu():
    print('|| Add a book to the library: enter "1" || Create student: enter "2" || Exit: enter "0" ||')
    try:
        command = int(input('Please enter the command:'))
        return command
    except ValueError:
        print("Please enter correct menu number!")


def teacher_workflow(active_teacher):
    active = True
    while active:
        command = teacher_menu()
        if command == 1:
            name = input('Please enter the name of book: ')
            year = input('Please enter year of book: ')
            author = input('Please enter the name of author: ')
            location = input('Please enter the shelf number you are going to place book: ')
            active_teacher.add_book(name, year, author, location)
        elif command == 2:
            name = input('Please enter the name of student: ')
            password = input('Please enter password for student: ')
            st_class = input('Please enter the class of student: ')
            active_teacher.create_student(name, password, st_class)
        elif command == 0:
            print("Session finished!")
            active = False
        else:
            print('Please enter correct menu number!')


def workflow():
    active = True
    while active:
        command = menu()
        if command == 1:
            start_student()
        elif command == 2:
            start_teacher()
        elif command == 0:
            print("Session finished!")
            active = False
        else:
            print('Please enter correct menu number!')


def get_password(name):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM USERS WHERE NAME=?''', (name,))
    data = cursor.fetchone()
    try:
        return [data[2], data[4]]
    except Exception:
        return False


def check_pass_student(name, password):
    user_pass = get_password(name)
    if user_pass:
        if user_pass[0] == password and user_pass[1] and user_pass[1] != "NULL":
            return True
    else:
        return False


def check_pass_teacher(name, password):
    user_pass = get_password(name)
    if user_pass:
        if user_pass[0] == password and user_pass[1] and user_pass[1] == "NULL":
            return True
    else:
        return False


def start_student():
    name = input('Please enter name: ')
    password = input('Please enter password: ')
    if check_pass_student(name, password):
        active_student = Student(name, 'Student')
        student_workflow(active_student)
    else:
        print("Wrong username and/or password!")


def start_teacher():
    name = input('Please enter name: ')
    password = input('Please enter password: ')
    if check_pass_teacher(name, password):
        active_teacher = Teacher(name, 'Teacher')
        teacher_workflow(active_teacher)
    else:
        print("Wrong username and/or password!")


def start():
    workflow()


start()


# st = Student('Anna Shmidt', 'Student')
# st.book_history()
# st.student_books()
# st.take_book()
# st.return_book()
# tc = Teacher('Ivanna Pemonenko', 'Teacher')
# tc.create_student('Olga Korotka', '1', '4F')
