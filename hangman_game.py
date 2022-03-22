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
    palabra_adivinando= "_"*len(normalize(read_data()))
    contador_vidas=0
    numero_vidas=len(normalize(read_data()))+5
    print("Tienes" , numero_vidas ," vidas")
    while palabra_adivinar != palabra_adivinando and contador_vidas!=numero_vidas:
        print(palabra_adivinando.upper())
        lyrics=str(input("Ingrese una letra: "))
        
        if lyrics in palabra_adivinar:
            palabra_adivinando=list(palabra_adivinando)
            for i,x in enumerate(palabra_adivinar):
                if x==lyrics:
                    palabra_adivinando[i]=x
            palabra_adivinando="".join(palabra_adivinando)      
        os.system('cls')
        
        if lyrics not in palabra_adivinar and contador_vidas!=numero_vidas:
            contador_vidas+=1
            print("Prueba con otra letra")
        print("Te quedan: " ,(numero_vidas - contador_vidas), " vidas")
    if palabra_adivinar== palabra_adivinando:           
        print("Felicitaciones GANASTE, la palabra era: "+ palabra_adivinando.upper())
    else:
        print("Perdiste, se te acabaron las vidas \n La palabra era : "+ palabra_adivinar.upper())
                  
if __name__=='__main__':   
    run()



