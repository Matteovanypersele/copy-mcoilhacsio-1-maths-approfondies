L'approche avec deux listes est la suivante :

```python
def arbre_additif(valeurs):
    niveau = [(None, x, None) for x in valeurs]
    
    while len(niveau) > 1:
        dessus = []
        for i in range(0, len(niveau), 2):
            gauche = niveau[i]
            droit = niveau[i + 1]
            somme = gauche[1] + droit[1]
            dessus.append((gauche, somme, droit))
        niveau = dessus
    
    return niveau[0]
```

L'approche récursive est plus subtile. On peut débuter en écrivant :

```python
def arbre_additif(valeurs):
    n = len(valeurs)
    
    if n == 1: 
        return (None, valeurs[0], None)
        
    return (arbre_additif(valeurs[:n//2]), sum(valeurs), arbre_additif(valeurs[n//2:]))
```

Toutefois, cette méthode a deux inconvénients :

* les sommes sont calculées à plusieurs reprises ;
* on crée de nombreuses copies partielles de la liste `valeurs` qui occupent inutilement la mémoire.

On peut palier ces deux problèmes à l'aide de la version ci-dessous :

```python
def arbre_additif(valeurs, debut=None, fin=None):
    if debut is None:
        debut = 0
        fin = len(valeurs)
        
    if fin - debut == 1:  # une seule valeur dans la zone d'étude
        return (None, valeurs[debut], None)

    milieu = (fin + debut) // 2
    gauche = arbre_additif(valeurs, debut, milieu)  # on travaille sur la moitié gauche
    droite = arbre_additif(valeurs, milieu, fin)  # on travaille sur la moitié droite
    somme = gauche[1] + droite[1]  # somme "efficace"
    
    return (gauche, somme, droite)
```

À chaque étape on n'additionne que les deux valeurs des nœuds inférieurs et on ne crée pas de copies de la liste en utilisant des indices désignant quelle zone prendre en compte dans chaque appel récursif.