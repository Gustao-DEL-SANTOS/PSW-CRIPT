from random import randint
from os import system as os


alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
af = str().join(alfabeto)
alfabetoUper = alfabeto
carcterSpecial = ['!', '\"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=',
                      '>', '?', '@', '[', '\ ', ']', '^', '_', '`', '{', '}', '~']

tipo = input('Digite quantidade de letras minusculas, maiusculas e caracteres especiais: ')

senha = ''
senha2 = ''
senha3 = ''
password = ''
alMin = int(tipo[0])
alMai = int(tipo[1])
chaSp = int(tipo[2])
sp = int(alMin) + int(alMai) + int(chaSp)


for i in range(alMin):
    senha += f'{alfabeto[randint(0, len(alfabeto)-1)]}'
for i in range(alMai):
    senha2 += f'{alfabetoUper[randint(0, len(alfabetoUper) - 1)]}'.upper()
for i in range(chaSp):
    senha3 += f'{carcterSpecial[randint(0, len(carcterSpecial)-1)]}'

for j in range(sp):
    if alMin > j:
        password += f'{senha[randint(0, len(senha)-1)]}'
    if alMai > j:
        password += f'{senha2[randint(0, len(senha2)-1)]}'
    if chaSp > j:
        password += f'{senha3[j]}'


# print(senha)
# print(senha2)
# print(senha3)
print(f'Senha gerada -> \" {password} \"')
os(f'MSG * SENHA:   " {password} " ')
salvar = input('Deseja salvar [S/N]: ').upper()
if salvar == 'S':
    senhaApp = input('Digite para qual aplicação sera essa senha: ')
    os(r'echo {} - {} >> senhas.txt'.format(senhaApp, password))
    os('echo hello >> pas.txt')
