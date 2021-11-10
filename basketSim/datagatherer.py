
successThrow = 0
failThrow = 0
successBlock = 0
failBlock = 0
rounds = 0
wildscores = 0


def collectHoopsGame2(offResult, defResult, score, cont):
    global successThrow
    global failThrow
    global successBlock
    global failBlock
    global rounds
    global wildscores

    if offResult:
        successThrow += 1

    if not offResult:
        failThrow += 1

    if defResult:
        successBlock += 1

    if not defResult:
        failBlock += 1

    if not offResult and not defResult:
        wildscores += 1

    if cont:
        rounds += 1



def resultHoopsGame2():
    print('Total Rounds: ' + str(rounds))
    print('Successful Throws: ' + str(successThrow))
    print('Failed Throws: ' + str(failThrow))
    print('Successful Blocks: ' + str(successBlock))
    print('Failed Blocks: ' + str(failBlock))
    print('Times Ball went wild: ' + str(wildscores))
