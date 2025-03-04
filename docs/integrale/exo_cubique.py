def f(x):
    return 0.5 * x**3 - 0.5 * x**2 - 0.5 * x + 1


def aire(a, b, n):
    somme = 0
    dx = (b - a) / n
    for k in range(n):
        x = a + k * dx
        somme = somme + f(x) * dx
    return somme

print("pour n = 2^3, aire = ", aire(-1, 2, 8))
print("pour n = 2^4, aire = ", aire(-1, 2, 16))
print("pour n = 2^10, aire = ", aire(-1, 2, 1024))
