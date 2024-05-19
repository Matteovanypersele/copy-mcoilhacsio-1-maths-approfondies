# --------- PYODIDE:env --------- #

def est_pair(n):
    return n % 2 == 0


# --------- PYODIDE:code --------- #

def filtre_pair(entiers):
    ...


# --------- PYODIDE:corr --------- #

def filtre_pair(entiers):
    return [nbre for nbre in entiers if est_pair(nbre)]


# --------- PYODIDE:tests --------- #

assert filtre_pair([1, 2, 3, 4, 5, 6, 7]) == [2, 4, 6]
assert filtre_pair([]) == []


# --------- PYODIDE:secrets --------- #

assert filtre_pair([100, 201, 302, 404, 501, 601, 700]) == [100, 302, 404, 700]
