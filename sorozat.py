import random


def lista_generalas():
    lista = []
    i = 0
    while i < 7:
        vel = random.randint(0,1)
        lista.append(bool(vel))
        i+=1
    return lista

def lista_kiiratas(lista):
    i = 0
    szoveg = ""
    while i < len(lista):
        if lista[i]:
            szoveg += "FEJ"
        else:
            szoveg += "ÍRÁS"

        if i < len(lista) - 1:
            szoveg +="-"
        i+=1
    print(f"II/A, B, C:\n\t{szoveg}")


def fejek_szama(lista):
    i = 0
    db = 0
    while i < len(lista):
        if lista[i]:
            db+=1
        i+=1
    return db

def konzol_kiir(db):
    print(f"II/F:\n\tA fejek száma: {db}.")

def file_kiir(db):
    f = open("fejek.txt", "w", encoding="utf-8")
    f.write(f"II/F:\n\tA fejek száma: {db}.")
    f.close()