""" Øvelse: "Calculator"

Som altid, læs hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning i kopien.

-------

Opret et program, der fungerer som en simpel lommeregner. Programmet skal fungere som følger:
    1. Forklar brugeren hvordan man betjener programmet.
    2. Præsenter en menu med følgende muligheder:
        - Addition
        - Subtraktion
        - Multiplikation
        - Division
        - Afslut
    3. Bed brugeren om at vælge en mulighed fra menuen.
    4. Hvis brugeren vælger en aritmetisk operation, bed om to tal.
    5. Udfør den valgte operation og vis resultatet.
    6. Gentag processen, indtil brugeren vælger at afslutte.

-------

Hvis du går i stå, spørg Google, andre elever, en AI eller læreren.

Når dit program er færdigt, skub det til dit GitHub-repository.
"""
print("Hej velkommen til en lommerenger")
print("Du kan bruge følgne teng +, -, *, /")

def calc():
    print("----------------------------")
    while True:
        print("Vælg hvad du vil:")
        print("1: Addition")
        print("2: Subtraktion")
        print("3: Multiplication")
        print("4: Division")
        print("5: Afslut")

        choice = input("Skriv du vil: ")

        if choice == "5":
            print("Sov godt")
            break

        if choice not in ["1", "2", "3", "4", "5"]:
            print("Du har ikke skrevet en af mulighederne")
            continue

        while True:
            try:
                number1 = int(input("Skriv det første tal:  "))
                break
            except ValueError:
                print("Det var ikke et tal! Prøv igen.")

        while True:
            try:
                number2 = int(input("Skriv det andet tal:  "))
                break
            except ValueError:
                print("Det var ikke et tal! Prøv igen.")

        if choice == "1":
            result = number1 + number2
            op = "+"
        elif choice == "2":
            result = number1 - number2
            op = "-"
        elif choice == "3":
            result = number1 * number2
            op = "*"
        elif choice == "4":
            if number2 == 0 or number1 == 0:
                print("Det kan du ikke")
                continue
            result = number1 / number2
            op = "/"

        print(f"{number1} {op} {number2} = {result}")

calc()