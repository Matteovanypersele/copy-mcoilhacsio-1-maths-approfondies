def aire(n):
    somme = 0
    largeur = 1 / n
    for k in range(n):
        x = k * largeur
        somme = somme + x**2 * largeur
    return somme

print("pour n = 2^3, aire = ", aire(8))
print("pour n = 2^4, aire = ", aire(16))
print("pour n = 2^10, aire = ", aire(1024))
