import numpy as np
from numpy import random
from time import sleep


class Person:

    def __init__(self, name, team, hasBall, throwStat, defenseStat):
        self.name = name
        self.team = team
        self.hasBall = hasBall
        self.throwStat = throwStat
        self.defenseStat = defenseStat

    def __str__(self):
        return 'Player: {} \nThrowing: {}'.format(self.name,self.throwStat)

    def throwBall(self):
        success = random.randint(100)
        throwChance = 45 + (self.throwStat * 5)

        if self.hasBall == True:
            if success < throwChance:
                print(str(success) + " < " + str(throwChance))
                print(self.name + ' scores!')
                self.hasBall = False
                return 'a'

            else:
                print(str(success) + " > " + str(throwChance))
                print(self.name + ' misses!')
                self.hasBall = False
                return 'b'
        else:
            print(self.name + ' does not have a ball!')


def genPlayer(team):
    randThrow = random.randint(5)
    randDefense = random.randint(5)
    f = open(r'C:\Users\liter\Documents\GitHub\vault-of-code\basketSim\playernames.txt')
    name = f.readlines()
    randpick = random.randint(len(name))
    myPerson = Person(name[randpick].rstrip(), team, True, randThrow, randDefense)
    f.close()
    return myPerson

def genTeam():
    f = open(r"C:\Users\liter\Documents\GitHub\vault-of-code\basketSim\teamnames.txt")
    team = f.readlines()
    randpick = random.randint(len(team))
    i = 0
    while i < 3:
        genPlayer(team[randpick].rstrip())
        i += 1
        # Complete this function by saving the created player to a new txt file named after the selected team name.
        # If name already exists, overwrite that file.
    f.close()

def hoopsGame(Person, rounds):
    player = Person
    score = 0
    misses = 0
    cont = 0
    while cont < rounds:
        if player.hasBall == True:
            print(player.name + ' has the ball!')

        print(player.throwStat)

        result = player.throwBall()

        if result == 'a':
            score += 1
        elif result == 'b':
            misses += 1

        print('Score: ' + str(score))
        print('Misses: ' + str(misses))
        player.hasBall = True
        cont += 1
        print('')

        if score < misses:
            print(player.name + ' loses!')
        elif score > misses:
            print(player.name + ' wins!')
        else:
            print('Disapointing')

def main():
    player = genPlayer('off_team')
    print(player.name + ' enters the Court.')

    ##hoopsGame(player,10)

    print(player.__str__())

if __name__ == '__main__':
    main()
