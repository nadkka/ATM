import os

pin_bank=1234

plik=open("konto.txt", "r")
stan= int(plik.read())
plik.close()

def poprawny_pin(pin, pin_bank):
    return pin== pin_bank

def sukces():
    os.system('cls')
    print("Jesteś zalogowany")

def menu():
    print("\nCo chcesz zrobić?")
    print("""
    1. Sprawdź stan konta
    2. Wypłać
    3. Wpłać
    4. Wyloguj
    """)

def stank():
    global stan
    os.system('cls')
    print(f"Stan konta: {stan}")

def wyplac():
    global stan
    os.system('cls')
    while True:
        wyplata=int(input("Ile chcesz wyplacic? "))
        if stan>=wyplata:
            stan=stan-wyplata
            print(f"Wyplacono {wyplata} zł")
            print(f"Obecny stan konta: {stan}")
            plik=open("konto.txt", "w")
            plik.write(f"{stan}")
            plik.close()
            break
        if stan<wyplata:
            print("Nie masz wystarczająco pieniedzy! Popraw błąd!")
            


def wplac():
    global stan
    os.system('cls')
    wplata=int(input("Ile chcesz wplacic? "))
    stan= stan+ wplata
    print(f"Wyplacono {wplata} zł")
    print(f"Obecny stan konta: {stan}")
    plik=open("konto.txt", "w")
    plik.write(f"{stan}")
    plik.close()


while True:
    pin= int(input("PODAJ PIN: "))
    if poprawny_pin(pin, pin_bank):
        sukces()
        print("WITAJ W SYSTEMIE!")
        while True:
            menu()
            opcja= input("OPCJA: ")
            if opcja=="1":
                stank()
            elif opcja=="2":
                wyplac()
            elif opcja=="3":
                wplac()
            elif opcja=="4":
                break
            else:
                os.system("cls")
                print("Nie ma takiej opcji!")

