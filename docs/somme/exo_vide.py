# --------- PYODIDE:env --------- #

nombres = [1, 2, 3, 4, 5]


# --------- PYODIDE:code --------- #

def somme(ma_liste):
    ...


print(somme(nombres))

# --------- PYODIDE:corr --------- #

def somme(ma_liste):
    total = 0
    for nbre in ma_liste:
        total = total + nbre
    return total


# --------- PYODIDE:tests --------- #

assert somme(nombres) == 15
assert somme([]) == 0


# --------- PYODIDE:secrets --------- #

assert somme([1, 2, 3, 4, 5, 6, 7]) == 28
