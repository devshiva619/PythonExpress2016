from mathtools import is_prime, fibbo

total = 0

for i in fibbo(20):
    if is_prime(i):
        total += i

print total