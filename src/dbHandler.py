import sqlite3
from io import StringIO
from json import dump,load
import hashlib
import datetime


def getPath():
    path = './src/data.db'
    try:
        sqlite3.connect(path)
    except sqlite3.OperationalError:
        path = '../src/data.db'
    return path


def connect():
    path = getPath()
    return sqlite3.connect(path)



def createTables() -> None:
    
    connection = connect()
    cursor = connection.cursor()
    cursor.execute('PRAGMA foreign_keys=on;')
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
        bonneReponse TEXT,
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


def connectUser(username: str, password: str) -> bool or list:
    connection = connect()
    cursor = connection.cursor()

    res = cursor.execute(
        """select pseudo,mdp, estAdmin from Utilisateur where pseudo=? and mdp=?""", (username, password))
    connection.commit()

    res = res.fetchone()
    connection.close()

    if res == None:
        return False
    else:
        return res
    
def createAccount(username :str, password : str, estAdmin : int)-> bool:
    connection = connect()
    cursor = connection.cursor()
    password = hashlib.md5(password.encode('utf-8')).hexdigest()
    try:

        cursor.execute('''insert into Utilisateur(pseudo,mdp,estAdmin) values (?,?,?)''',
                       (username, password, estAdmin))
        connection.commit()
        connection.close()
        return True

    except sqlite3.IntegrityError:  # si l'utilisateur existe déjà
        return False
    
def createQuizz(nameQuizz : str, type : str)-> bool:
    connection = connect()
    cursor = connection.cursor()
    try:
        cursor.execute('''insert into Quizz(idQuizz,type) values (?,?)''', (nameQuizz, type))
        connection.commit()
        connection.close()
        return True
    except sqlite3.IntegrityError:
        return False
    
    
def createQuestion(nameQuestion, listeProposition, bonneRep, idQuizz) -> bool:
    connection = connect()
    cursor = connection.cursor()
    cursor.execute('PRAGMA foreign_keys=on;')
    #serialize 'listeProposition'
    buffer = StringIO()
    res = dump(listeProposition, buffer)
    listeProposition = buffer.getvalue()
    try:
        cursor.execute('''insert into Questions(question, proposition, bonneReponse, idQuizz) values (?,?,?,?)''', (nameQuestion,listeProposition,bonneRep, idQuizz))
        connection.commit()
        connection.close()
        return True
    except sqlite3.IntegrityError:
        return False
    

def majScore(idQuizz,pseudo,nbpoints):
        
    connection = connect()
    cursor = connection.cursor()
    cursor.execute('PRAGMA foreign_keys=on;')
    currentDate = datetime.datetime.now()
    try:
        cursor.execute('''insert into Score(idQuizz, pseudo, nbpoints, date) values (?,?,?,?)''', (idQuizz,pseudo, nbpoints, currentDate))
        connection.commit()
        connection.close()
        return True
    except sqlite3.IntegrityError:
        return False

def queryQuestions(idQuizz,idQuest):
    connection = connect()
    cursor = connection.cursor()
    try:
        res = cursor.execute('''select idQuest, question, proposition, bonneReponse, idQuizz from Questions where idQuizz=? and idQuest=?''', (idQuizz,idQuest))
        connection.commit()
        res =res.fetchone()
        #désérialiser
        res = list(res)
        buffer = StringIO(res[2])
        read = load(buffer)
        res[2] = read
        
        return res
    except sqlite3.IntegrityError:
        return False
    
def queryScore(pseudo):
    connection = connect()
    cursor = connection.cursor()
    try:
        res = cursor.execute('''select idScore,idQuizz,pseudo,nbpoints,date from Score where pseudo=?''', (pseudo,))
        connection.commit()
        res =res.fetchall()
        print(res)
    except sqlite3.IntegrityError:
        return False
    

if __name__ == '__main__':
    queryScore('ugo')


# def queryQuestions(quizzName):
    # connection = connect()
#     cursor = connection.cursor()

#     cursor.execute('select ')

#     connection.commit()
#     connection.close()


# def updateCollection()
