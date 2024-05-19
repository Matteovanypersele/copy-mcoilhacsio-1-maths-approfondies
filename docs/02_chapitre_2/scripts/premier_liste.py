# --------- PYODIDE:env --------- #


# --------- PYODIDE:code --------- #

def premier(ma_liste):
    ...


# --------- PYODIDE:corr --------- #

def premier(ma_liste):
    return ma_liste[0]


# --------- PYODIDE:tests --------- #

assert premier([8, 4, 6]) == 8


# --------- PYODIDE:secrets --------- #

assert premier([9, 4, 6, 15]) == 9
assert premier([200, 4, 6, 15]) == 200
