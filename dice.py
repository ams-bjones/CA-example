import random

class dice:
    def __init__(self, top = 6):
        self.top = top
        self.score = 1
    
    def roll(self):
        self.score = random.randint(1,self.top)
    
    def __repr__(self):
        return(str(self.score))
        
dices = [dice(), dice(4), dice(12)]
playing = True
while playing:
    print('you have {0} dice\n'.format(len(dices)))
    for ind, die in enumerate(dices, start =1):
        print('dice {0}, reads {1}'.format(ind, die.score))
    print('Which die would you like to roll?')
    choice = input ('please enter the die number, a for all, or x to exit. ')
    choice = str(choice)
    if choice.isnumeric():
        choice = int(choice)
        choice = choice -1
        dices[choice].roll()
    elif 'x' in choice:
        playing = False
    elif 'a' in choice:
        for die in dices:
            die.roll()
    