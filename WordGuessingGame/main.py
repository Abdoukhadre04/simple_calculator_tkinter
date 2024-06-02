import random

name = input('Quel est votre nom ? : ')

print('Bonne chance', name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks'
         ]

randWord = random.choice(words)

val = input('Entrer une lettre alphabet: ')

if val in randWord:
    print('La lettre', val, 'est dans le mot')
    