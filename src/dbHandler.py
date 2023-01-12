import sqlite3


def connect():
    return sqlite3.connect('src/data.db')


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

def connect_user(username :str, password : str) -> False or list:
    connection = connect()
    cursor = connection.cursor()
    
    
    res = cursor.execute("""select pseudo,mdp, estAdmin from Utilisateur where pseudo=? and mdp=?""", (username,password))
    connection.commit()    
    
    res = res.fetchone()
    connection.close()
    
    if res == None:
        return False
    else:
        return res
    
def create_account(username :str, password : str,confirmPassword, estAdmin : int)-> None:
    connection = connect()
    cursor = connection.cursor()
    try:
        if password == confirmPassword:
            cursor.execute('''insert into Utilisateur(pseudo,mdp,estAdmin) values (?,?,?)''', (username, password, estAdmin))
            connection.commit()
            connection.close()
            return (username, password, estAdmin)
        else:
            return False

    except sqlite3.IntegrityError: #si l'utilisateur existe déjà
        return False
    
def create_quizz(nameQuizz : str, ):
        
    pass
    
if __name__ == '__main__':
    print((create_account('freeze', 'polytech', 'polytech', 1)))


# def queryQuestions(quizzName):
    # connection = connect()
#     cursor = connection.cursor()

#     cursor.execute('select ')

#     connection.commit()
#     connection.close()


# def updateCollection()
