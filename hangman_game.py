from asyncore import read
from distutils.command.clean import clean
import os
import random
words={}
numero_random=random.randint(0,171)
def read_data():
        with open(r"C:\Users\EQUIPO\documents\PROYECTOS_PERSONALES\juego_del_ahorcado\data.txt", encoding="utf-8") as f:
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
def run():
    palabra_adivinar=normalize(read_data())
    print(palabra_adivinar)
    palabra_adivinando= "_"*len(normalize(read_data()))
    while palabra_adivinar != palabra_adivinando:
        print(palabra_adivinando)
        lyrics=str(input("Ingrese una letra: "))
        if lyrics in palabra_adivinar:
            palabra_adivinando=list(palabra_adivinando)
            for i,x in enumerate(palabra_adivinar):
                if x==lyrics:
                    palabra_adivinando[i]=x
                    palabra_adivinando="".join(palabra_adivinando)           
    print("Felicitaciones GANASTE")
                    
    
run()



