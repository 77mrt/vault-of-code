
successThrow = 0
failThrow = 0
successBlock = 0
failBlock = 0
rounds = 0


def collectHoopsGame2(offResult, defResult, score, cont):
    global successThrow
    global failThrow
    global successBlock
    global failBlock
    global rounds
    global firstRound

    if offResult == 'a':
        successThrow += 1

    if offResult == 'b':
        failThrow += 1

    if not defResult:
        successBlock += 1

    if (offResult == 'b' and not defResult) or defResult:
        failBlock += 1

    if cont:
        rounds += 1



def resultHoopsGame2():
    print('Total Rounds: ' + str(rounds))
    print('Successful Throws: ' + str(successThrow))
    print('Failed Throws: ' + str(failThrow))
    print('Successful Blocks: ' + str(successBlock))
    print('Failed Blocks: ' + str(failBlock))
