"""opgave: Objektorienteret rollespil, afsnit 2 :

Som altid skal du læse hele øvelsesbeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Byg videre på din løsning af afsnit 1.

Del 1:
    Opfind to nye klasser, som arver fra klassen Character. For eksempel Hunter og Magician.
    Dine nye klasser skal have deres egne ekstra metoder og/eller attributter.
    Måske overskriver de også metoder eller attributter fra klassen Character.

Del 2:
    Lad i hovedprogrammet objekter af dine nye klasser (dvs. rollespilfigurer) kæmpe mod hinanden,
    indtil den ene figur er død. Udskriv, hvad der sker under kampen.

I hver omgang bruger en figur en af sine evner (metoder). Derefter er det den anden figurs tur.
Det er op til dig, hvordan dit program i hver tur beslutter, hvilken evne der skal bruges.
Beslutningen kan f.eks. være baseret på tilfældighed eller på en smart strategi

Del 3:
    Hver gang en figur bruger en af sine evner, skal du tilføje noget tilfældighed til den anvendte evne.

Del 4:
    Lad dine figurer kæmpe mod hinanden 100 gange.
    Hold styr på resultaterne.
    Prøv at afbalancere dine figurers evner på en sådan måde, at hver figur vinder ca. halvdelen af kampene.

Hvis du går i stå, kan du spørge google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""

import random

class Character:
    all_character = []

    def __init__(self, name, max_health, attackpower, team):
        self.name = name
        self.max_health = max_health
        self.attackpower = attackpower
        self.team = team
        self._current_health = max_health
        Character.all_character.append(self)

    def __repr__(self):
        return f"Character: Name {self.name}| Max health {self.max_health}| Health {self._current_health}| Attackpower {self.attackpower}"

    def hit(self, other):
        other.get_hit(self.attackpower, self.name)

    def get_hit(self, attack, name):
        chance = random.randint(1, 10)
        if chance == 1:
            print(f"Oh {name} missed {self.name}")
        elif chance == 2:
            attack *= 3
            self._current_health -= attack
            if self._current_health < 0:
                self._current_health = 0
            print(f"⚔️⚔️ {name} hits {self.name} with a critical hit for {attack} damage! ({self._current_health}/{self.max_health} HP left) ⚔️⚔️")
        else:
            self._current_health -= attack
            if self._current_health < 0:
                self._current_health = 0
            print(f"⚔️ {name} hits {self.name} for {attack} damage! ({self._current_health}/{self.max_health} HP left)")

    def get_healed(self, heal, name):
        chance = random.randint(1, 10)
        health_before = self._current_health

        if chance == 1:
            print(f"Oh {name} coulndt heal {self.name}")
        else:
            self._current_health += heal
            if self._current_health > self.max_health:
                self._current_health = self.max_health

            health_after = self._current_health
            healed_amount = health_after - health_before

            if self._current_health == self.max_health:
                print(f"➕ {name} heals {self.name} for {healed_amount} HP | {self.name} is at max health ({self._current_health}/{self.max_health})")
            else:
                print(f"➕ {name} heals {self.name} for {healed_amount} HP ({self._current_health}/{self.max_health} HP)")

    def get_magichit(self, magicpower, name):
        chance = random.randint(1, 4)
        if chance == 1:
            magicpower /= 2
            magicpower = int(magicpower)
            for character in Character.all_character:
                if character.team == self.team:
                    character._current_health -= magicpower
                    if character._current_health < 0:
                        character._current_health = 0
            print(f"✨ {name} hits the enntire enemy team for {magicpower} HP ✨")
        else:
            self._current_health -= magicpower
            if self._current_health < 0:
                self._current_health = 0
            print(f"✨ {name} hits {self.name} for {magicpower} HP ({self._current_health}/{self.max_health})")

    def get_assasinhit(self, name, attack):
        if self._current_health <= 25:
            attack = self._current_health
            self._current_health -= attack
            if self._current_health < 0:
                self._current_health = 0
            print(f"💀 {self.name} got assainated by {name}")
        else:
            self._current_health -= attack
            if self._current_health < 0:
                self._current_health = 0
            print(f"💀 {name} hits {self.name} for {attack} damage! ({self._current_health}/{self.max_health} HP left)")

class Healer(Character):
    def __init__(self, name, max_health, healpower, team):
        super().__init__(name, max_health, 0, team)
        self.healpower = healpower

    def __repr__(self):
        return f"Healer: Name {self.name}| Max health {self.max_health}| Health {self._current_health}| Healpower {self.healpower}"

    def heal(self, other):
        other.get_healed(self.healpower, self.name)

class Mage(Character):
    def __init__(self, name, max_health, magicpower, team):
        super().__init__(name, max_health, 0, team)
        self.magicpower = magicpower

    def __repr__(self):
        return f"Mage: Name {self.name}| Max health {self.max_health}| Magicpower {self.magicpower}"

    def magichit(self, other):
        other.get_magichit(self.magicpower, self.name)

class Assasin(Character):
    def __init__(self, name, max_health, attackpower, team):
        super().__init__(name, max_health, attackpower, team)

    def __repr__(self):
        return f"Assasin: Name {self.name} | Max health {self.max_health}| Attackpower {self.attackpower}"

    def assasinhit(self, other):
        other.get_assasinhit(self.name, self.attackpower)

def alive(character):
    return [c for c in character if c._current_health > 0]

hero1 = Character("Hero1", 100, 5, 1)
healer1 = Healer("Healer1", 100, 10, 1)
mage1 = Mage("Mage1", 50, 10, 1)
assasin1 = Assasin("Assasin1", 50, 10, 1)
hero2 = Character("Hero2", 100, 5, 2)
healer2 = Healer("Healer2", 100, 10, 2)
mage2 = Mage("Mage2", 50, 10, 2)
assasin2 = Assasin("Assasin2", 50, 10, 2)

turn = 0
winner = 0
while not winner:
    turn += 1

    alive_team1 = alive([hero1, mage1, assasin1, healer1])
    alive_team2 = alive([hero2, mage2, assasin2, healer2])

    if not alive_team1:
        winner = "Team 2"
        break
    if not alive_team2:
        winner = "Team 1"
        break

    actor = random.choice(alive_team1)
    if isinstance(actor, Healer):
        heal_targets = [c for c in alive_team1 if c != actor]
        if heal_targets:
            actor.heal(random.choice(heal_targets))
    else:
        if alive_team2:
            target = random.choice(alive_team2)
            if isinstance(actor, Mage):
                actor.magichit(target)
            elif isinstance(actor, Assasin):
                actor.assasinhit(target)
            else:
                actor.hit(target)

    actor = random.choice(alive_team2)
    if isinstance(actor, Healer):
        heal_targets = [c for c in alive_team2 if c != actor]
        if heal_targets:
            actor.heal(random.choice(heal_targets))
    else:
        if alive_team1:
            target = random.choice(alive_team1)
            if isinstance(actor, Mage):
                actor.magichit(target)
            elif isinstance(actor, Assasin):
                actor.assasinhit(target)
            else:
                actor.hit(target)

    print(f"\n╔════════════ TURN {turn} ════════════╗")

    print("║ TEAM 1")
    print(f"║   {hero1.name:10} HP: {hero1._current_health:3}/{hero1.max_health}")
    print(f"║   {mage1.name:10} HP: {mage1._current_health:3}/{mage1.max_health}")
    print(f"║   {assasin1.name:10} HP: {assasin1._current_health:3}/{assasin1.max_health}")
    print(f"║   {healer1.name:10} HP: {healer1._current_health:3}/{healer1.max_health}")

    print("║")
    print("║ TEAM 2")
    print(f"║   {hero2.name:10} HP: {hero2._current_health:3}/{hero2.max_health}")
    print(f"║   {mage2.name:10} HP: {mage2._current_health:3}/{mage2.max_health}")
    print(f"║   {assasin2.name:10} HP: {assasin2._current_health:3}/{assasin2.max_health}")
    print(f"║   {healer2.name:10} HP: {healer2._current_health:3}/{healer2.max_health}")

    print("╚═════════════════════════════════╝")

if winner:
    print(f"\n══════════ Winner {winner} ══════════")