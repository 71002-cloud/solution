"""Opgave "Lunar arithmetic"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

--------

Denne øvelse er en valgfri udfordring for de fremragende programmører blandt jer.
Du behøver absolut ikke at løse denne øvelse for at fortsætte med succes.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Del 1:
    Se de første 3 minutter af denne video:
    https://www.youtube.com/watch?v=cZkGeR9CWbk

Del 2:
    Skriv en klasse Lunar_int(), med metoder, der gør, at du kan anvende operatorerne + og * på
    objekter af denne klasse, og at resultaterne svarer til de regler, der forklares i videoen.

Del 3:
    Se resten af videoen.

Del 4:
    Skriv en funktion calc_lunar_primes(n), som retunerer en liste med de første n lunar primes.

--------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""


class Lunar_int():
    def __init__(self, value):
        if isinstance(value, int):
            self.value = str(value)
        elif isinstance(value, str) and value.isdigit():
            self.value = value
        else:
            raise ValueError("Lunar_int skal intitialiseres med et heltal eller streng af cifre")

    def __str__(self):
        return self.value

    def __repr__(self):
        return f"Lunar_int({self.value})"

    def __eq__(self, other):
        if isinstance(other, Lunar_int):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == str(other)
        elif isinstance(other, str):
            return self.value == other
        else:
            return False

    def __pad_value(self, other):
        a, b = self.value, str(other)
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        return a, b

    def __add__(self, other):
        a, b = self.__pad_value(other)
        result = ''.join(str(max(int(x), int(y))) for x, y in zip(a, b))
        return Lunar_int(result)

    def __mul__(self, other):
        other_str = str(other)
        total = Lunar_int(0)
        for i, d in enumerate(reversed(other_str)):
            interm = ''.join(str(min(int(x), int(d))) for x in self.value)
            interm += '0' * i
            total += Lunar_int(interm)
        return total


def lunar_mul(a, b):
    a = Lunar_int(a)
    b = Lunar_int(b)
    result = a * b
    return result

def lunar_primes(n):
    prime_list = []
    result_list = []
    start = 19
    for i in range(1, 999):
        if i == 9:
            continue
        else:
            for o in range(1, 999):
                if o == 9:
                    continue
                result = lunar_mul(i, o)
                result_list.append(result)
    while len(prime_list) < n:
        a = Lunar_int(start)
        if '9' in str(a) and not a in result_list and not a == 9:
            prime_list.append(a)
        start += 1

    prime_str = ' '.join(str(a) for a in prime_list)
    return prime_str

print(lunar_primes(99))


a = Lunar_int(19)
b = Lunar_int(29)

print(a + b)
print(a * b)