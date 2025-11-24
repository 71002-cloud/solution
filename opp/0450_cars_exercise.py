"""
Opgave "Cars":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Definer en funktion drive_car(), der udskriver en bils motorlyd (f.eks. "roooaar")

I hovedprogrammet:
    Definer variabler, som repræsenterer antallet af hjul og den maksimale hastighed for 2 forskellige biler
    Udskriv disse egenskaber for begge biler
    Kald derefter funktionen drive_car()

Hvis du ikke har nogen idé om, hvordan du skal begynde, kan du åbne 0460_cars_help.py og starte derfra.
Hvis du går i stå, kan du spørge google, de andre elever, en AI eller læreren.
Hvis du stadig er gået i stå, skal du åbne 0470_cars_solution.py og sammenligne den med din løsning.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""

bil_1_hjul = 4
bil_1_maxspeed = 160

bil_2_hjul = 6
bil_2_maxspeed = 160

def drive_car():
    print("Kachowwww")

print(f"Bil 1 har {bil_1_hjul} hjul og en top fart på {bil_1_maxspeed} km/h")
print(f"Bil 2 har {bil_2_hjul} hjul og en top fart på {bil_2_maxspeed} km/h")
drive_car()