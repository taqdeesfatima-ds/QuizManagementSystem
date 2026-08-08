import sqlite3
import hashlib

def create_database():

    connection = sqlite3.connect("database/quiz.db")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS admins(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT NOT NULL UNIQUE,

            password TEXT NOT NULL

        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS questions(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            question TEXT NOT NULL,

            option_a TEXT NOT NULL,

            option_b TEXT NOT NULL,

            option_c TEXT NOT NULL,

            option_d TEXT NOT NULL,

            correct_answer TEXT NOT NULL

        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            roll_number TEXT NOT NULL UNIQUE,

            email TEXT NOT NULL

        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS results(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            student_id INTEGER NOT NULL,

            score INTEGER NOT NULL,

            total_questions INTEGER NOT NULL

        )
    """)
    connection.commit()
    
    connection.close()
def create_admin():

    connection = sqlite3.connect("database/quiz.db")

    cursor = connection.cursor()

    try:

        cursor.execute(
            """
            INSERT INTO admins(username, password)
            VALUES(?, ?)
            """,
            ("admin", "admin123")
        )

        connection.commit()

        print("Admin created successfully.")

    except sqlite3.IntegrityError:

        print("Admin already exists.")

    connection.close()

def register_admin(username, password):

    connection = sqlite3.connect("database/quiz.db")

    cursor = connection.cursor()

    password_hash = hashlib.sha256(
        password.encode()
    ).hexdigest()

    try:

        cursor.execute(
            """
            INSERT INTO admins(username, password)
            VALUES(?, ?)
            """,
            (username, password_hash)
        )

        connection.commit()

        connection.close()

        return True

    except sqlite3.IntegrityError:

        connection.close()

        return False
def verify_admin(username, password):

    connection = sqlite3.connect("database/quiz.db")

    cursor = connection.cursor()

    password_hash = hashlib.sha256(
        password.encode()
    ).hexdigest()

    cursor.execute(
        """
        SELECT * FROM admins
        WHERE username = ? AND password = ?
        """,
        (username, password_hash)
    )

    admin = cursor.fetchone()

    connection.close()

    return admin

def add_question(question, option_a, option_b, option_c, option_d, correct_answer):

    connection = sqlite3.connect("database/quiz.db")

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO questions
        (question, option_a, option_b, option_c, option_d, correct_answer)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (question, option_a, option_b, option_c, option_d, correct_answer)
    )

    connection.commit()

    connection.close()

def get_all_questions():

    connection = sqlite3.connect("database/quiz.db")

    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM questions
    """)

    questions = cursor.fetchall()

    connection.close()

    return questions

def update_question(
    question_id,
    question,
    option_a,
    option_b,
    option_c,
    option_d,
    correct_answer
):

    connection = sqlite3.connect("database/quiz.db")

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE questions
        SET
            question = ?,
            option_a = ?,
            option_b = ?,
            option_c = ?,
            option_d = ?,
            correct_answer = ?
        WHERE id = ?
        """,
        (
            question,
            option_a,
            option_b,
            option_c,
            option_d,
            correct_answer,
            question_id
        )
    )

    connection.commit()

    connection.close()

def delete_question(question_id):

    connection = sqlite3.connect("database/quiz.db")

    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM questions
        WHERE id = ?
        """,
        (question_id,)
    )

    connection.commit()

    connection.close()

def search_questions(keyword):

    connection = sqlite3.connect("database/quiz.db")

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT * FROM questions
        WHERE question LIKE ?
        """,
        ("%" + keyword + "%",)
    )

    questions = cursor.fetchall()

    connection.close()
 
    return questions

def get_all_students():

    connection = sqlite3.connect("database/quiz.db")

    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM students
    """)

    students = cursor.fetchall()

    connection.close()

    return students

def save_result(student_id, score, total_questions):

    connection = sqlite3.connect("database/quiz.db")

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO results
        (student_id, score, total_questions)
        VALUES (?, ?, ?)
        """,
        (student_id, score, total_questions)
    )

    connection.commit()

    connection.close()

def get_all_results():

    connection = sqlite3.connect("database/quiz.db")

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            results.id,
            students.name,
            students.roll_number,
            results.score,
            results.total_questions
        FROM results
        INNER JOIN students
        ON results.student_id = students.id
    """)

    results = cursor.fetchall()

    connection.close()

    return results
  
def delete_result(result_id):

    connection = sqlite3.connect("database/quiz.db")

    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM results
        WHERE id = ?
        """,
        (result_id,)
    )

    connection.commit()

    connection.close()

if __name__ == "__main__":
    create_database()
    create_admin()
