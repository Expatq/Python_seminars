from math import gcd


class Fraction:
    def reduce(self):
        g = gcd(self.num, self.denum)
        self.num //= g
        self.denum //= g

        return self


    def __init__(self, s:str): #numerator and denumerator
        if '/' in s:
            s = s.split('/')
        else:
            s = s.split()

        self.num = int(s[0])
        try:
            self.denum = int(s[1])
        except IndexError:
            self.denum = 1

        self.reduce()


    def __str__(self):
        if self.denum != 1:
            return f"{self.num}/{self.denum}"
        else:
            return f"{self.num}"


    def __lt__(self, other):
        if isinstance(other, (int, float)):
            return self.num < other * self.denum

        elif isinstance(other, Fraction):
            return self.num * other.denum < other.num * self.denum


    def __add__(self, other):
        res_num = self.num * other.denum + other.num * self.denum
        res_denum = self.denum * other.denum

        result = Fraction(f"{res_num}/{res_denum}")

        return result



print(Fraction("1 2"))
print(Fraction("4 16"))
print(Fraction("14/7"))
print(Fraction("5"))
print(Fraction("45/25"))

a = (Fraction("1 2"))
b = (Fraction("3/7"))
print(a < b)
print(a + b)

c = (Fraction("4 3"))
arr = [a, b, c]
arr.sort()
for x in arr:
    print(x, end = ' ')