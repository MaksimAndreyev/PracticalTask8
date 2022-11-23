import output


def chooseCommand(request, dossiers):
    if request == 'список':
        output.printDossiers()
    elif request == 'поиск':
        name = output.askInput('Введите имя: ')
        for i in dossiers:
            if i[1] == name:
                print(*i)
    elif request == 'добавить':
        employee = list(output.askInput('Введите данные нового сотрудника: ').split())
        dossiers.append(employee)
        with open('data.txt', 'w', encoding='utf8') as f:
            result = []
            for i in dossiers:
                result.append(' '.join(i)+'\n')
            f.writelines(result)
