# --- PYODIDE:env --- #
# Import de matplotlib (installation lors du 1er lancement)
import matplotlib

# Précision du backend à utiliser
matplotlib.use("module://matplotlib_pyodide.html5_canvas_backend")

# Insertion de la courbe dans une div spécifié(id="cible_2")
from js import document 
document.pyodideMplTarget = document.getElementById("cible_2")
# On vide la div
document.getElementById("cible_2").textContent = ""

# --- PYODIDE:code --- #

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
xs = [-2 + k * 0.1 for k in range(41)]
ys = [x**3 for x in xs]
ax.plot(xs, ys, "r-")
plt.title("La fonction cube")
plt.show()
