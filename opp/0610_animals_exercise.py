import random

class Animal:
    def __init__(self, name, sound, height, weight, legs, female):
            self.name = name
            self.sound = sound
            self.height = height
            self.weight = weight
            self.legs = legs
            self.female = female

    def __repr__(self):
        return f"Animal: {self.name}, {self.sound}, {self.height} cm, {self.weight} kg, {self.legs}, {self.female}"

    def make_noise(self):
            print(self.sound)

class Dog(Animal):
    def __init__(self, name, sound, height, weight, legs, female, taillenght, huntssheeps):
            super().__init__(name, sound, height, weight, legs, female)
            self.taillenght = taillenght
            self.huntssheeps =  huntssheeps

    def __repr__(self):
        return f"Dog: {self.name}, {self.sound}, {self.height} cm, {self.weight} kg, {self.legs}, {self.female}, {self.huntssheeps}, {self.taillenght} cm"

    def wag_tail(self):
        print (f"Hunden {self.name} vifter med sin {self.taillenght} cm lange hale")

def mate(mother, father):

    if mother.female and not father.female or not mother.female and father.female:

        name = "Puppy"
        sound = random.choice([mother.sound, father.sound])
        height = int(random.uniform(min(mother.height, father.height), max(mother.height, father.height)))
        weight = int(random.uniform(min(mother.weight, father.weight), max(mother.weight, father.weight)))
        legs = 4
        female = random.choice([True, False])
        taillenght = int(random.uniform(min(mother.taillenght, father.taillenght), max(mother.taillenght, father.taillenght)))
        huntssheeps = random.choice([mother.huntssheeps, father.huntssheeps])

        return Dog(name, sound, height, weight, legs, female, taillenght, huntssheeps)

    else:
        return "Tror ikke du har lært hvordan man laver børn, det skal være en af hver køn"

bob = Animal("Bob", "Rawr", 200, 2000, 2, False)
bob.make_noise()
print(bob)

print("---------------------------------------------------")

fido = Dog("Fido", "woof", 50, 80, 4, False, 20, False)
fido.make_noise()
fido.wag_tail()
print(fido)

print("---------------------------------------------------")

women = Dog("Women dog", "anden hunde lyd", 70, 180, 4, True, 25, False)
women.make_noise()
women.wag_tail()
print(women)

print("---------------------------------------------------")

print(mate(women, fido))