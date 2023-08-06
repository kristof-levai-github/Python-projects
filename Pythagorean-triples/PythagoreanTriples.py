limit = 100

found_triple = None

for a in range(1, limit):
    for b in range(a + 1, limit):
        c = (a**2 + b**2)**0.5
        if c <= limit and abs(a - b) == 10 and int(c) == c:
            found_triple = (a, b, int(c))
            break

if found_triple:
    a, b, c = found_triple
    print(f"{a}, {b}, {c}")
else:
    print("No such Pythagorean triple with a difference of 10 exists within the specified limit.")
