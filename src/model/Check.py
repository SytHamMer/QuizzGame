from QuestionMaker import *

#This file will take the answer give by the user and check if it's right or false
#we suppose here that questions is an object with attribut : questions,propositions (list), good answer
def verification(data,answer):
    """check if the answer is good

    Args:
        data (Question): all info about questions
        answer (string): answer give by the user

    Returns:
        boolean: true -> good answer
    """
    if data.goodAnswer == answer:
        return True
    else:
        return False

def correction(data,bool):
    """Correct the answer

    Args:
        data (Question): all info about questions
        bool (boolean): Output of verification(data,answer)

    Returns:
        string: good answer or a success message
    """
    if bool == True:
        res = "Vous avez donné la bonne réponse !"
    else:
        res = data.goodAnswer

    return res

if __name__ == "__main__":
    test = Question("Qui est le/la plus gentil.le ?",["Ugo","Arnaud","Lila","Mathys"],"Mathys")
    print(verification(test,"Lila"))
    print(correction(test,verification(test,"Lila")))