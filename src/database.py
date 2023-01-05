import sqlite3

conn = sqlite3.connect('src/ma_base.db')

cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS Score(

    idScore INTEGER PRIMARY KEY UNIQUE,
    date DATE



)

""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS Utilisateur(

    pseudo TEXT PRIMARY KEY UNIQUE,
    mdp VARCHAR(250),
    estAdmin BOOLEAN,
    idScore INT,
    FOREIGN KEY(idScore) REFERENCES Score(idScore)



)

""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Questions(
    idQuest INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    question TEXT,
    proposition VARCHAR(250),
    bonne_reponse TEXT
  

)

""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Quizz(
    idQuizz INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    nom TEXT,
    type TEXT,
    image VARCHAR(250),
    idQuest INT,
    FOREIGN KEY(idQuest) REFERENCES Questions(idQuest)

)

""")



cursor.execute("""
CREATE TABLE IF NOT EXISTS joue(
    iduti TEXT,
    idQuizz INT,
    nbpoints INT,
    PRIMARY KEY(iduti, idQuizz)
    FOREIGN KEY(iduti) REFERENCES Utilisateur(pseudo)
    FOREIGN KEY(idQuizz) REFERENCES Score(idQuizz)
)
""")





conn.commit()


