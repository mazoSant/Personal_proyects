from asyncore import read
import random
words={}
numero_random=random.randint(0,171)
def read_data():
        with open(r"C:\Users\EQUIPO\documents\juego_del_ahorcado\data.txt", encoding="utf-8") as f:
            words=[word.strip('\n') for word in f] #Here eliminated the espaces (Saltos de linea) y ennumere las palabras en el diccionario
            words=dict(enumerate(words))
            return words.get(numero_random)
def normalize(s):
        replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),)
        for a, b in replacements:
            s = s.replace(a, b).replace(a.upper(), b.upper())
        return s

print(normalize(read_data()))


