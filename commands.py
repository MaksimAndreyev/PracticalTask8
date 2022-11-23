import output


def chooseCommand(request, dossiers):
    if request == 'список':
        output.printDossiers()
    elif request == 'поиск':
        name = output.askInput('Введите имя: ')
        for i in dossiers:
            if i[1] == name:
                print(*i)
