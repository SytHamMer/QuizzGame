from QuestionMaker import *

#This file will take the answer give by the user and check if it's right or false
#we suppose here that questions is an object with attribut : questions,propositions (list), good answer
def verification(data,answer):
    """In : object Question, and answer give
    OUT: Boolean"""
    if data.goodAnswer == answer:
        return True
    else:
        return False

def correction(data,bool):

    """In: Object Question, and verification()
    Out: String to show to the user"""
    if bool == True:
        res = "Vous avez donné la bonne réponse !"
    else:
        res = data.goodAnswer

    return res

if __name__ == "__main__":
    test = Question("Qui est le/la plus gentil.le ?",["Ugo","Arnaud","Lila","Mathys"],"Mathys")
    print(verification(test,"Lila"))
    print(correction(test,verification(test,"Lila")))