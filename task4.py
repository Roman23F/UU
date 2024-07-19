# "4st program"
a = 13.42
b = 42.13
print(int(a) == int(b % 42 * 100) or int(b) == int(a % 13 * 100))
