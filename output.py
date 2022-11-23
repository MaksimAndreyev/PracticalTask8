def askInput(message):
    return input(message).lower()


def printDossiers():
    with open('data.txt', 'r', encoding='utf8') as f:
        for i in f:
            print(i, end='')
