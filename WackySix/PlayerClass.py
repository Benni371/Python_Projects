class Player:
    def __init__(self,name):
        self.round = 1
        self.roundScores = []
        self.name = name
        self.totalScore = sum(self.roundScores)
    def addScores(self, score):
        self.roundScores.append(score)
        self.totalScore = sum(self.roundScores)

    def editScore(self, adjustment,position):
        '''
        adjustment: the amount to adjust the score by(Negative or positive number)
        position: to the user this represent the round score that was scored incorrectly
        '''
        # user will enter a digit that is position that is from 1-6
        # to get the right index minus one
        position -= 1
        # find that position in the array. add a negative or positive number
        # that adjust to the correct value
        self.roundScores[position] += adjustment
    def displayAllScores(self):
        for i in self.roundScores:
            print(i)
