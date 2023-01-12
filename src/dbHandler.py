import sqlite3
import os


def connect():
    path = os.path.abspath("../data.db")
    return sqlite3.connect(path)


def createTables() -> None:
    connection = connect()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Utilisateur(
        pseudo TEXT PRIMARY KEY UNIQUE,
        mdp TEXT,
        estAdmin NUMERIC
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Quizz(
        idQuizz TEXT PRIMARY KEY UNIQUE,
        type TEXT,
        image VARCHAR(250)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Questions(
        idQuest INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        question TEXT,
        proposition VARCHAR(250),
        bonne_reponse TEXT,
        idQuizz TEXT,
        FOREIGN KEY(idQuizz) REFERENCES Quizz(idQuizz)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Score(
        idScore INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        idQuizz TEXT,
        pseudo TEXT,
        nbpoints INT,
        date DATE,
        FOREIGN KEY(pseudo) REFERENCES Utilisateur(pseudo),
        FOREIGN KEY(idQuizz) REFERENCES Quizz(idQuizz)
    )
    """)

    connection.commit()
    connection.close()

# def query(sql: str) -> None:
    # connection = connect()
#     cursor = connection.cursor()

#     # cursor.execute(sql)

#     connection.commit()
#     connection.close()


# def queryQuestions(quizzName):
    # connection = connect()
#     cursor = connection.cursor()

#     cursor.execute('select ')

#     connection.commit()
#     connection.close()


# def updateCollection()
