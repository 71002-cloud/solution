"""
Opgave "Morris The Miner" (denne gang objekt orienteret)

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Genbrug din oprindelige Morris-kode og omskriv den til en objektorienteret version.

Definer en klasse Miner med attributter som sleepiness, thirst osv.
og metoder som sleep, drink osv.
Opret Morris og initialiser hans attributter ved at kalde konstruktoren for Miner:
morris = Miner()

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
."""

class Miner:
    def __init__(self):
        self.turn = 0
        self.sleepiness = 0
        self.thirst = 0
        self.hunger = 0
        self.gold = 0
        self.whisky = 0

    def __str__(self):
        return (
            f"turn {self.turn}, "
            f"sleepiness {self.sleepiness}, "
            f"thirst {self.thirst}, "
            f"hunger {self.hunger}, "
            f"whisky {self.whisky}, "
            f"gold {self.gold}"
        )

    def sleep(self):
        self.sleepiness -= 10
        self.thirst += 1
        self.hunger += 1

    def mine(self):
        self.sleepiness += 5
        self.thirst += 5
        self.hunger += 5
        self.gold += 5

    def eat(self):
        self.sleepiness += 5
        self.thirst += 5
        self.hunger -= 20
        self.gold -= 2

    def buy_whisky(self):
        self.sleepiness += 5
        self.thirst += 1
        self.hunger += 1
        self.gold -= 1
        self.whisky += 1

    def drink(self):
        self.sleepiness += 5
        self.thirst -= 15
        self.hunger += 1
        self.whisky -= 1

    def dead(self):
        return self.sleepiness > 100 or self.thirst > 100 or self.hunger > 100

morris = Miner()

while not morris.dead() and morris.turn < 1000:
    morris.turn += 1

    if morris.sleepiness > 90:
        morris.sleep()
        action = "Morris sleeps"
    elif morris.thirst > 90 and morris.whisky > 0:
        morris.drink()
        action = "Morris drinks"
    elif morris.hunger > 90 and morris.gold >= 2:
        morris.eat()
        action = "Morris eats"
    elif morris.whisky < 5 and morris.gold >= 1 and morris.turn < 976:
        morris.buy_whisky()
        action = "Buys whisky"
    else:
        morris.mine()
        action = "Morris mines"

    print(action)
    print(morris)
    print("--------------------------------------------------------------------------------")