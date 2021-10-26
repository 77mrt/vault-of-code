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

    def savePlayer(self):
        return '{} {} {} {} {}'.format(self.name,self.team,self.hasBall,self.throwStat,self.defenseStat)

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
    myPerson = Person(name[randpick].rstrip(), team, False, randThrow, randDefense)
    f.close()
    return myPerson

def genTeam():
    f = open(r"C:\Users\liter\Documents\GitHub\vault-of-code\basketSim\teamnames.txt")
    team = f.readlines()
    randpick = random.randint(len(team))
    tName = team[randpick].rstrip()
    newFile = "C:/Users/liter/Documents/GitHub/vault-of-code/basketSim/teamslog/" + tName + ".txt"
    i = 0
    t = open(newFile, 'w')
    while i < 3:
        addPlayer = genPlayer(tName)
        t.write(addPlayer.savePlayer()+"\n")
        i += 1
    t.close()
    t2 = open(newFile,'r')
    roster = t2.readlines()
    f.close()
    print(roster)
    return "The " + tName +"\n"

def hoopsGame(Person, rounds):
    player = Person
    score = 0
    misses = 0
    cont = 0
    player.hasBall = True
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
        sleep(3)
        print('')

    if score < misses:
        print(player.name + ' loses!')
    elif score > misses:
        print(player.name + ' wins!')
    else:
        print('Disapointing')

def main():
    #player = genPlayer('off_team')
    #print(player.name + ' enters the Court.')

    #hoopsGame(player,10)

    #print(player.__str__())

    team = genTeam()
    print(team)

if __name__ == '__main__':
    main()
