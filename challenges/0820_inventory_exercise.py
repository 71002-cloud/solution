"""Opgave "The inventory sequence"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

--------

Denne øvelse er en valgfri udfordring for de fremragende programmører blandt jer.
Du behøver absolut ikke at løse denne øvelse for at fortsætte med succes.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Del 1:
    Se de første 3 minutter af denne video:
    https://www.youtube.com/watch?v=rBU9E-ZOZAI

Del 2:
    Skriv en funktion inventory(), som producerer de tal, der er vist i videoen.
    Funktionen accepterer en parameter, der definerer, hvor mange talrækker der skal produceres.
    Funktionen udskriver tallene i hver række.

    Du vil sandsynligvis ønske at definere en funktion count_number(), som tæller, hvor ofte
    et bestemt antal optræder i den aktuelle talrække.

Del 3:
    I hovedprogrammet kalder du inventory() med fx 6 som argument.

Hvis du ikke har nogen idé om, hvordan du skal begynde, kan du kigge på løsningen
i 0822_inventory_solution.py

--------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""

inventory_array = []

def menu():
    while True:
        print("\n--- Inventory Sequence Menu ---")
        print("1. Run Inventory()")
        print("2. Show full inventory")
        print("3. Count occurrences of a number")
        print("4. Reset inventory")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            try:
                nm = int(input("How many rounds should I run Inventory()? "))
                inventory(nm)
            except ValueError:
                print("Please enter a valid integer.")

        elif choice == "2":
            print(f"Full inventory: {inventory_array}")

        elif choice == "3":
            try:
                nm = int(input("Which number do you want to count? "))
                count = count_number(nm)
                print(f"The number {nm} appears {count} times in the inventory.")
            except ValueError:
                print("Please enter a valid integer.")

        elif choice == "4":
            inventory_array = []
            print("Inventory reset. Current inventory:", inventory_array)

        elif choice == "5":
            print("Bye bye!")
            break

        else:
            print("Invalid choice. Please select 1-5.")


def inventory(number):
    for i in range(number):
        k = 0
        round_list = []
        while True:
            count = inventory_array.count(k)
            round_list.append(count)
            inventory_array.append(count)
            if count == 0:
                break
            k += 1
        print(f"{round_list} - Round list")

    print(f"{inventory_array} - Full list")

def count_number(number):
    return inventory_array.count(number)

menu()