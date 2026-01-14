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