from random import randint
from os import system
from time import sleep

def porgetes(currBal: int) -> int:
    system('cls')

    tetek = menu(currBal)
    if(tetek == -1): return -1
    szorzo = tetek[3]

    loadingAnim()

    porgetSzam = randint(0, 36)
    nyert = nyertes(tetek, porgetSzam)

    if (nyert): currBal += tetek[0] * szorzo
    else: currBal -= tetek[0]

    print(f"Porgetett szam:\n{porgetSzam}")
    return currBal

def menu(bal: int) -> int:
    print("Rulett Játék -------------")
    print("Udvozlunk a jatekban, tegyen fel tetet egy izgalmas francia rulettben!")
    print(f"Jelenegi vagyona: {bal} Ft.-")
    rakottTet = tetBeker(bal)

    if (rakottTet == -1):
        return -1

    system('cls')

    while True:
        jatekValasztas = input("Valasszon mire szeretne tetet rakni -\n1 - Felek (1x)\n2 - Tucatok (2x)\n3 - Oszlopok (2x)\n4 - Konkret szam (35x)\n5 - Szinek (1x)\n")
        
        system('cls')
        
        if (jatekValasztas.isnumeric()):
            manager = jatekManager(jatekValasztas)
            valasztas = manager[0]
            szorzo = manager[1]
            break
        else:
            print("Helytelenul valasztott!")

    return rakottTet, int(jatekValasztas), valasztas.upper(), int(szorzo)

def tetBeker(currentBalance: int) -> int:
    while True:
        bekertTet = input(f"Adjon meg tetet (maximum {currentBalance}):")
        if (bekertTet.isnumeric()):
            bekertTet = int(bekertTet)
            if (bekertTet <= currentBalance and bekertTet > 0):
                break
            print("Nem tud ennyit feltenni! Adjon megujra egy tet osszeget!")
        else:
            print("Helytelen tet mennyiseget adott meg!")
    return bekertTet

def nyertes(userInput: list, nyertesSzam: int) -> bool:
    jatek = userInput[1]
    valasztottJatek = userInput[2]
    nyert = False
    match jatek:
        case 1:
            if( (nyertesSzam <= 1 and nyertesSzam <= 18 and valasztottJatek == 'E') or (nyertesSzam <= 19 and nyertesSzam >= 36 and valasztottJatek == 'M') ): nyert = True
        case 2:
            if( (nyertesSzam <= 1 and nyertesSzam >= 12 and valasztottJatek == 'A') or (nyertesSzam <= 13 and nyertesSzam >= 24 and valasztottJatek == 'B') or (nyertesSzam <= 25 and nyertesSzam >= 36 and valasztottJatek == 'C')): nyert = True
        case 3:
            if( ((nyertesSzam % 3) == 1 and valasztottJatek == 'A') or ((nyertesSzam % 3) == 2 and valasztottJatek == 'B') or ((nyertesSzam % 3) == 0 and valasztottJatek == 'C') or nyertesSzam != 0): nyert = True
        case 4:
            if(nyertesSzam == int(valasztottJatek)): nyert = True
        case 5:
            fekSzamok = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
            szamFekete = nyertesSzam in fekSzamok
            if( (szamFekete == True and valasztottJatek == "F") or (szamFekete == False and valasztottJatek == "P")): nyert = True
    return nyert

def jatekManager(jatek: str) -> list[str, int]:
    multi = 1
    kapottvalasz = ""
    match int(jatek):
        case 1:
            kapottvalasz = input("Felek - Adja meg melyik felre akarja rakni a tetet!\nE ~ 1-18\nM ~ 19-36\n")
        case 2:
            kapottvalasz = input("Tucatok - Adja meg melyik tucatra szeretne rakni tetet!\nA ~ 1-12\nB ~ 13-24\nC ~ 25-36\n")
            multi = 2
        case 3:
            kapottvalasz = input("Oszlopok - Adja meg melyik oszlopra akarja rakni a tetet!\nA ~ 1, 4, 7 ...\nB ~ 2, 5, 8 ...\nC ~ 3, 6, 9 ...\n")
            multi = 2
        case 4:
            kapottvalasz = input("Konkret Szam - Adjon meg egy szamot amire rakni akarja a tetet! (0-36)\n")
            multi = 35
        case 5:
            kapottvalasz = input("Szinek - Adja meg melyik szinre akarja rakni a tetet!\nP - piros szin\nF - fekete szin\n")
    return kapottvalasz, multi

def loadingAnim() -> None:
    for i in range(0, 9, 1):
        if(i == 1 or i == 5 or i == 9):
            print("Porgetes folyamatban .")
            print("-")
        elif(i == 2 or i == 6):
            print("Porgetes folyamatban ..")
            print("\ ")
        elif (i == 3 or i == 7): 
            print("Porgetes folyamatban ...")
            print("|")
        else:
            print("Porgetes folyamatban .")
            print("/")
        sleep(0.3)
        system('cls')

def main() -> None:
    balance = 1000

    while True:
        try:
            balance = porgetes(balance)
            print(f"Uj vagyona: {balance}")


            if(balance <= 0):
                print("Csodbe mentel!")
                break

            folytatas = input("Folytatni akarja? (I/N)")
            if(folytatas.upper() == "N" or folytatas == "0"):
                system('cls')
                print(f"Szerzett penz - {balance - 1000}")
                break

        except KeyboardInterrupt:
            system('cls')
            print("Gyors kilépés ----")
    
    print("Viszlát!")
    sleep(1)
    system('cls')
main()