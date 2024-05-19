# --------- PYODIDE:code --------- #

def est_pair(n)
    ...

# --------- PYODIDE:corr --------- #

def est_pair(n)
    return n % 2 == 0


# --------- PYODIDE:tests --------- #

assert est_pair(42) is True
assert est_pair(1) is False


# --------- PYODIDE:secrets --------- #

assert est_pair(0) is True
assert est_pair(2001) is False
