

# --------- PYODIDE:env --------- #

from collections import deque


def creer_file():
    """Crée et renvoie une file vide"""
    return deque([])


def enfiler(file, valeur):
    """Enfile valeur dans file"""
    file.append(valeur)


def defiler(file):
    """Défile et renvoie la valeur en tête de file"""

    return file.popleft()

# --------- PYODIDE:code --------- #

def arbre_additif(valeurs):
    ...

# --------- PYODIDE:corr --------- #

def arbre_additif(valeurs):
    file = creer_file()
    for x in valeurs:
        noeud = (None, x, None)
        enfiler(file, noeud)

    while len(file) > 1:
        gauche = defiler(file)
        droite = defiler(file)
        somme = gauche[1] + droite[1]
        enfiler(file, (gauche, somme, droite))

    return defiler(file)

# --------- PYODIDE:tests --------- #

assert arbre_additif([6]) == (None, 6, None)
assert arbre_additif([6, 9]) == ((None, 6, None), 15, (None, 9, None))
assert arbre_additif([3, 5, 7, 4]) == (
    ((None, 3, None), 8, (None, 5, None)),
    19,
    ((None, 7, None), 11, (None, 4, None)),
)

# --------- PYODIDE:secrets --------- #


# Tests supplémentaires
from random import randrange

def __arbre_additif__(valeurs):
    file = creer_file()
    for x in valeurs:
        noeud = (None, x, None)
        enfiler(file, noeud)

    while len(file) > 1:
        gauche = defiler(file)
        droite = defiler(file)
        somme = gauche[1] + droite[1]
        enfiler(file, (gauche, somme, droite))

    return defiler(file)

for _ in range(10):
    nb_feuilles = 2 ** randrange(3, 10)
    valeurs = [randrange(-100, 101) for _ in range(nb_feuilles)]
    attendu = __arbre_additif__(valeurs)
    assert arbre_additif(valeurs) == attendu, f"Erreur avec {valeurs}"