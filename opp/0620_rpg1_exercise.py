import random
"""Opgave: Objektorienteret rollespil, afsnit 1 :

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Del 1:
    Definer en klasse "Character" med attributterne "name", "max_health", "_current_health", "attackpower".
    _current_health skal være en protected attribut, det er ikke meningen at den skal kunne ændres udefra i klassen.

Del 2:
    Tilføj en konstruktor (__init__), der accepterer klassens attributter som parametre.

Del 3:
    Tilføj en metode til udskrivning af klasseobjekter (__repr__).

Del 4:
    Tilføj en metode "hit", som reducerer _current_health af en anden karakter med attackpower.
    Eksempel: _current_health=80 og attackpower=10: et hit reducerer _current_health til 70.
    Metoden hit må ikke ændre den private attribut _current_health i en (potentielt) fremmed klasse.
    Definer derfor en anden metode get_hit, som reducerer _current_health for det objekt, som den tilhører, med attackpower.

Del 5:
    Tilføj en klasse "Healer", som arver fra klassen Character.
    En healer har attackpower=0 men den har en ekstra attribut "healpower".

Del 6:
    Tilføj en metode "heal" til "Healer", som fungerer som "hit" men forbedrer sundheden med healpower.
    For at undgå at "heal" forandrer den protected attribut "_current_health" direkte,
    tilføj en metode get_healed til klassen Character, som fungerer lige som get_hit.

Hvis du er gået i stå, kan du spørge google, de andre elever, en AI eller læreren.
Hvis du ikke aner, hvordan du skal begynde, kan du åbne 0622_rpg1_help.py og starte derfra.

Når dit program er færdigt, skal du skubbe det til dit github-repository
og sammenlign det med lærerens løsning i 0624_rpg1_solution.py
"""
from argparse import Action


class Character:

    name = ""
    max_health = 0
    _current_health = 0

    def __init__(self, name, max_health, attackpower):
        self.name = name
        self.max_health = max_health
        self.attackpower = attackpower
        self._current_health = max_health

    def __repr__(self):
        return f"Character: Name {self.name}| Max health {self.max_health}| Health {self._current_health}| Attackpower {self.attackpower}"

    def hit(self, other):
        other.get_hit(self.attackpower, self.name)

    def get_hit(self, attack, name):
        self._current_health -= attack
        if self._current_health < 0:
            self._current_health = 0

        print(
            f"💥 {name} hits {self.name} for {attack} damage! ({self._current_health}/{self.max_health} HP left)")

    def get_healed(self, heal, name):
        health_before = self._current_health
        self._current_health += heal
        if self._current_health > self.max_health:
            self._current_health = self.max_health

        health_after = self._current_health

        healed_amount = health_after - health_before

        if self._current_health == self.max_health:
            print(
                f"✨ {name} heals {self.name} for {healed_amount} HP | {self.name} is at max health ({self._current_health}/{self.max_health})")
        else:
            print(
                f"✨ {name} heals {self.name} for {healed_amount} HP ({self._current_health}/{self.max_health} HP)")

class Healer(Character):
    def __init__(self, name, max_health, healpower):
        super().__init__(name, max_health, 0)
        self.healpower = healpower

    def __repr__(self):
        return f"Healer: Name {self.name}| Max health {self.max_health}| Health {self._current_health}| Healpower {self.healpower}"

    def heal(self, other):
        other.get_healed(self.healpower, self.name)

hero1 = Character("Hero1", 100, 5)
hero2 = Character("Hero2", 100, 5)
healer1 = Healer("Healer1", 100, 10)
healer2 = Healer("Healer2", 100, 10)

turn = 0
winner = 0
while not winner:

    turn += 1

    if hero1._current_health <= 0:
        winner = "Team 2"
    elif hero1._current_health < hero1.max_health and random.randint(1, 4) == 3 and healer1._current_health > 0:
        healer1.heal(hero1)
    else:
        hero1.hit(random.choice([hero2, healer2]))

    if hero2._current_health <= 0:
        winner = "Team 1"
    elif hero2._current_health < hero2.max_health and random.uniform(1, 4) == 3 and healer2._current_health > 0:
        healer2.heal(hero2)
    else:
        hero2.hit(random.choice([hero1, healer1]))

    print(f"\n╔════════════ TURN {turn} ════════════╗")

    print("║ TEAM 1")
    print(f"║   {hero1.name:10} HP: {hero1._current_health:3}/{hero1.max_health}")
    print(f"║   {healer1.name:10} HP: {healer1._current_health:3}/{healer1.max_health}")

    print("║")
    print("║ TEAM 2")
    print(f"║   {hero2.name:10} HP: {hero2._current_health:3}/{hero2.max_health}")
    print(f"║   {healer2.name:10} HP: {healer2._current_health:3}/{healer2.max_health}")

    print("╚═════════════════════════════════╝")

if winner:
    print(f"\n══════════ Winner {winner} ══════════")