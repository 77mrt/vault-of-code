# import numpy as np
# from numpy import random
import random
import datagatherer
from time import sleep


class Person:

    def __init__(self, name, team, hasBall, throwStat, defenseStat):
        self.name = name
        self.team = team
        self.hasBall = hasBall
        self.throwStat = throwStat
        self.defenseStat = defenseStat

    def __str__(self):
        return 'Player: {} \nThrowing: {} \nDefense: {}'.format(self.name, self.throwStat, self.defenseStat)

    def savePlayer(self):
        return '{} {} {} {} {}'.format(self.name, self.team, self.hasBall, self.throwStat, self.defenseStat)

    def throwBall(self):
        success = random.randint(0, 100)
        throwChance = 45 + (self.throwStat * 5)

        if self.hasBall == True:
            if success < throwChance:
                print(str(success) + " < " + str(throwChance))
                print(self.name + ' takes the shot!')
                self.hasBall = False
                return True

            else:
                print(str(success) + " > " + str(throwChance))
                print(self.name + ' fumbles!')
                self.hasBall = False
                return False
        else:
            print(self.name + ' does not have a ball!')

    def blockThrow(self):
        success = random.randint(0, 100)
        blockChance = 45 + (self.defenseStat * 5)

        if success < blockChance:
            print(str(success) + " < " + str(blockChance))
            print(self.name + ' blocks the shot!')
            return True
        elif success > blockChance:
            print(str(success) + " > " + str(blockChance))
            print(self.name + ' whiffs!')
            return False


def genPlayer(team):
    randThrow = random.randint(1, 5)
    randDefense = random.randint(1, 5)
    f = open(r'C:\Users\liter\Documents\GitHub\vault-of-code\basketSim\playernames.txt')
    name = f.readlines()
    randpick = random.randint(0, len(name) - 1)
    print(randpick)  # delete later
    myPerson = Person(name[randpick].rstrip(), team, False, randThrow, randDefense)
    f.close()
    return myPerson


def genTeam():
    f = open(r"C:\Users\liter\Documents\GitHub\vault-of-code\basketSim\teamnames.txt")
    team = f.readlines()
    # randpick = random.randint(len(team))
    tName = ""
    r = 1
    for i in team:
        print(str(r) + ". " + i)
        r += 1

    errorCheck = False
    while not errorCheck:
        pick = int(input("Select a team: "))
        if len(team) < pick <= 0:
            print("Not a team. Select again.")
        else:
            print(team[pick - 1])
            tName = team[pick - 1].rstrip()
            errorCheck = True

    newFile = "C:/Users/liter/Documents/GitHub/vault-of-code/basketSim/teamslog/" + tName + ".txt"
    i = 0
    t = open(newFile, 'w')
    while i < 3:
        addPlayer = genPlayer(tName)
        t.write(addPlayer.savePlayer() + "\n")
        i += 1
    t.close()
    t2 = open(newFile, 'r')
    roster = t2.readlines()
    f.close()
    print(roster)


def readTeamFromFile(teamName):
    newFile = "C:/Users/liter/Documents/GitHub/vault-of-code/basketSim/teamslog/" + teamName + ".txt"
    f = open(newFile, 'r')
    list = f.readlines()
    i = 0
    teamlist = []
    while i < 3:
        parse = list[i].split()
        currPlayer = Person(parse[0], parse[1], bool(parse[2]), int(parse[3]), int(parse[4]))
        teamlist.append(currPlayer)
        i += 1
    return teamlist


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

        if result:
            score += 1
        elif not result:
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


def hoopsGame2(offPlayer, defPlayer, maxScore):
    score = 0
    rounds = 0
    offPlayer.hasBall = True
    while score < maxScore:
        if offPlayer.hasBall:
            print(offPlayer.name + ' has the ball!')
        else:
            print(offPlayer.name + ' does not have the ball!')
            break

        offense = offPlayer.throwBall()
        defense = defPlayer.blockThrow()

        if offense and defense:
            print(defPlayer.name + ' saves it! The game continues.')
            offPlayer.hasBall = True
        elif offense and not defense:
            print(offPlayer.name + ' scores!')
            score += 1
            offPlayer.hasBall = True
        elif not offense and defense:
            print(defPlayer.name + ' grabs the ball! ' + defPlayer.name + ' passes it back.')
            offPlayer.hasBall = True
        elif not offense and not defense:
            print('The ball is wild!')
            randBasket = random.randint(0,100)
            if randBasket > 95:
                print('The ball falls in anyway. ' + offPlayer.team + ' scores!')
                score += 1
            else:
                print('The ball falls out of bounds.')
            offPlayer.hasBall = True

        rounds += 1
        datagatherer.collectHoopsGame2(offense,defense,score,True)
        print('Round: ' + str(rounds))
        print('Score: ' + str(score))
        #sleep(3)
        print('')

    datagatherer.resultHoopsGame2()
    print('Game Over')

def main():
    player1 = Person('Cal', 'off_team', False, 3, 1)
    print(player1.name + ' enters the Court.')
    print(player1.__str__())

    player2 = Person('Ibis', 'def_team', False, 1, 1)
    print(player2.name + ' enters the Court.')
    print(player2.__str__())
    print('')
    hoopsGame2(player1, player2, 3)
    # hoopsGame(player,10)

    # print(player.__str__())
    # genTeam()
    # team1 = readTeamFromFile('Rockets')
    # i = 0
    # while i < len(team1):
    #    print(team1[i].__str__())
    #    i += 1


if __name__ == '__main__':
    main()
