""" Opgave "Number guessing"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

--------

Opret et program, der spiller et gættespil med brugeren. Programmet fungerer på følgende måde:
    Forklar reglerne for brugeren.
    Generer tilfældigt et 4-cifret heltal.
    Bed brugeren om at gætte et 4-cifret tal.
    Hvert ciffer, som brugeren gætter korrekt i den rigtige position, tæller som en sort mønt.
    Hvert ciffer, som brugeren gætter korrekt, men i den forkerte position, tæller som en hvid mønt.
    Når brugeren har gættet, udskrives det, hvor mange sorte og hvide mønter gættet er værd.
    Lad brugeren gætte, indtil gættet er korrekt.
    Hold styr på antallet af gæt, som brugeren gætter i løbet af spillet, og print det ud til sidst.

--------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""

import random

def menu():
    print("Vil du spille et spil?")
    anwser = input('Type "Ja" hvis du vil:  ')
    if anwser.lower() == "ja":
        game()
    else:
        print("Det var ikke et ja, sov godt")

def game():
    print("Jeg tænker på et 4 cifret tal")
    print("Kan du gætte det?")

    random_number = random.randint(1000, 9999)
    turn = 0
    win = False

    while not win:
        while True:
            try:
                user_guss = int(input("Gæt tallet:  "))
                if 1000 <= user_guss <= 9999:
                    turn += 1
                    break
                else:
                    print("Tallet skal være mellem 1000 og 9999")
            except ValueError:
                print("Det var ikke et tal! Prøv igen.")

        random_digits = [int(d) for d in str(random_number)]
        guess_digits = [int(d) for d in str(user_guss)]

        black = 0
        white = 0

        for i in range(4):
            if guess_digits[i] == random_digits[i]:
                black += 1

        for d in set(guess_digits):
            white += min(guess_digits.count(d), random_digits.count(d))

        white -= black

        if user_guss == random_number:
            print(f"Du vandt! Tallet var {random_number} som du nok havde gætted!")
            print(f"Du brugte {turn} forsøg")
            break
        else:
            print(f"Sorte mønter: {black}")
            print(f"Hvide mønter: {white}")
            print("Prøv igen")

    if input('Vil du spille igen? "Ja" for at fortsætte:  ').lower() == 'ja':
        game()
    else:
        print("Det var ikke et ja, sov godt")

menu()