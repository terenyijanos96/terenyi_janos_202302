from Epulet import *

def beolvas():
    f = open("epulet.txt", "r", encoding="utf-8")
    fejlec, tartalom = f.readline(), f.readlines()
    f.close()

    epulet_lista = []

    i = 0
    while i < len(tartalom):
        sor = tartalom[i].strip().split("$")
        epulet_lista.append(Epulet(sor))
        i+=1

    return epulet_lista

def epuletek_szama(lista):
    db = len(lista)
    print(f"III/A, B:\n\tAz épületek száma: {db}")
    return db

def otszazotvenot_labnal_magasabb_szama(lista):
    i = 0
    db = 0
    while i < len(lista):
        if 555 < (lista[i].magassag * 3.280839895):
            db+=1
        i+=1
    print(f"III/C:\n\tAz 555 lábnál magasabb épületek száma: {db}.")
    return db

def legoregebb_epulet(lista):
    legoregebb = 0
    i = 1
    while i < len(lista):
        aktualis = i
        if lista[aktualis].epules_eve < lista[legoregebb].epules_eve:
            legoregebb = aktualis
        i+=1
    kimenet = lista[legoregebb].orszag
    print(f"III/D:\n\tA legöregebb épület országa: {kimenet}.")
    return kimenet