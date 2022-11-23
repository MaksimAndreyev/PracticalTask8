import commands
import output
dossiers = []
with open('data.txt', 'r', encoding='utf8') as f:
    for i in f:
        dossiers.append(list(i[:-1].split()))
while True:
    inp = output.askInput('Введите комманду: ')
    if inp == 'стоп':
        break
    commands.chooseCommand(inp, dossiers)
