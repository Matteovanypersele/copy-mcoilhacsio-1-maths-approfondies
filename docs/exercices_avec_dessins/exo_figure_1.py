# --- PYODIDE:env --- #
# Import de matplotlib (installation lors du 1er lancement)
import matplotlib

# Précision du backend à utiliser
matplotlib.use("module://matplotlib_pyodide.html5_canvas_backend")

# Insertion de la courbe dans une div spécifié(id="cible_1")
from js import document 
document.pyodideMplTarget = document.getElementById("cible_1")
# On vide la div
document.getElementById("cible_1").textContent = ""

# --- PYODIDE:code --- #

import matplotlib.pyplot as plt

fig, ax = plt.subplots() # Syntaxe obligatoire pour ne pas mélanger plusieurs graphiques
xs = [-3 + k * 0.1 for k in range(61)]
ys = [x**2 for x in xs]
ax.plot(xs, ys, "r-")  # Syntaxe obligatoire pour ne pas mélanger plusieurs graphiques
plt.grid()  # Optionnel : pour voir le quadrillage
plt.axhline()  # Optionnel : pour voir l'axe des abscisses
plt.axvline()  # Optionnel : pour voir l'axe des ordonnées
plt.title("La fonction carré")
plt.show()
