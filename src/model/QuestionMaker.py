class Question:

    def __init__(self,question,propositions,goodAnswer):
        self.question = question
        self.propositions = propositions
        self.goodAnswer = goodAnswer


    def getQuestion(self):
        return self.question
    
    def getGoodAnswer(self):
        return self.goodAnswer

    def getPropositions(self):
        return self.propositions
