from faker import Faker
import PySimpleGUI as psg
import clipboard as c

psg.theme('DarkBlue1')

lyt = [
    [psg.Text('Clique em gerar e depois em copiar', size=(30, 1))],
    [psg.Button('gerar'), psg.Button('copiar'), psg.Button('fechar')],
    [psg.Text(key='nicks')]
]

wind = psg.Window('Gerador de nicks', lyt, finalize=True)
fk = Faker()
nick = ''

while True:
    e, v = wind.read()
    if e == psg.WIN_CLOSED:
        break
    if e == 'gerar':
        nick = fk.simple_profile()['username']
        wind['nicks'].update(nick)
    if e == 'copiar':
        c.copy(nick)
        nick = nick + ' (copiado) (>‿◠)' if not ' (copiado) (>‿◠)' in nick else nick
        wind['nicks'].update(nick)
    if e == 'fechar':
        break
wind.close()
