---
author: Mireille
title: QCM 1
tags:
  - qcm
  - Difficulté **
---

{{ multi_qcm(
    [
"""On donne la table de vérité suivante :

|a|b|?|
|:----:|:----:|:----:|
|F|F|V|
|F|V|V|
|V|F|V|
|V|V|F|

A quelle expression logique correspond cette table de vérité
""",
        [
            "NON (a OU b)",
            "a OU b",
            "a ET b",
            "NON (a ET b)",
        ],
        [4],
    ],
    [
        "Le résultat de l'addition des deux nombres binaires 1101 et 0101 est:",
        [
            "10110",
            "11010",
            "10010",
            "10011",
        ],
        [3],
    ],
    [
        "Donner l'écriture binaire du nombre 34",
        [
            "100001",
            "100110",
            "100010",
            "010010",
        ],
        [3],
    ],
    [
"""Le réel $x$ est représenté par le code suivant avec la norme IEEE 764 :
1 10001000110 1010 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
On rappelle que $x=(-1)^s . m . 2^{e-1023}$ avec $s$ le bit de signe, $e$ codé sur 11 bits, $m=1,f$   avec $f$ codé sur 52 bits.
Le réel $x$ est égal à :
""",
        [
            "$-1,625 . 2^{71}$",
            "$-1,625 . 10^{71}$",
            "$1,625 . 2^{72}$",
            "$1,625 . 10^{71}$",
            "$-1,625 . 2^{72}$",
            "Autre réponse",
        ],
        [1],
    ],
    [
"""
On a saisi le code suivant :
```python title=''
n = 8
while n > 1:
    n = n / 2
```

Que vaut `n` après l'exécution du code ?
""",
        [
            "2.0",
            "4.0",
            "1.0",
            "0.5",
        ],
        [3],
    ],
    [
        "Que vaut :  `#!py [(a,b) for a in range(1, 3) for b in range(a)]`",
        [
            "`#!py [(1, 0), (2, 1), (2, 1)]`",
            "`#!py [(1, 0), (2, 0), (2, 1)]`",
            "`#!py [(1, 0), (2, 1), (3, 2)]`",
            "`#!py [(0, 0), (1, 1), (2, 2)]`",
        ],
        [2],
    ],
    [
"""
On a saisi le code suivant :

```python title=''
def mystere(a, b):
    reponse = 1
    if a == 0:
        if b == 0:
            reponse = 0
    return reponse
```

A quoi est évalué `#!py mystere(0, 1)` ?
""",
        [
            "`#!py 0`",
            "`#!py False`",
            "`#!py True`",
            "`#!py 1`",
        ],
        [4],
    ],
    [
"""
On définit un tableau `#!py t` rempli de 0 en langage Python. Ce tableau est une liste de listes, toutes les sous-listes ayant le même nombre d'éléments.

```python title=''
t = [ [0, 0, …, 0],
      [0, 0, …, 0],
      …
      [0, 0, …, 0]]
```

On appelle `#!py h` le nombre de listes contenus dans `#!py t`et `#!py l` le nombre d'éléments appartenant à ces listes.
Parmi les propositions suivantes, laquelle permet de calculer `#!py h` et `#!py l` ?
""",
        [
            "`#!py h, l = len(t[0]), len(t)`",
            "`#!py h, l = len(t), len(t[0])`",
            "`#!py h, l = len(t[0]), len(t[1])`",
            "`#!py h, l = len(t[1]), len(t[0])`",
        ],
        [2],
    ],
    [
"""
`#!py liste_eleves` est une liste de listes contenant les notes d’élèves.
Le premier élément de chaque liste de `#!py liste_eleves` est le nom de l’élève, le deuxième est sa note au premier devoir et le troisième sa note au deuxième devoir.

Quel code python permet d’obtenir la liste des noms des élèves ayant eu strictement plus de 15 au deuxième devoir ?
""",
        [
            "`#!py [eleve[0] in liste_eleves if eleve[2] > 15]`",
            "`#!py [eleve for eleve in liste_eleves if eleve[2] > 15]`",
            "`#!py [eleve[0] for eleve in liste_eleves if eleve[2] > 15]`",
            "`#!py [eleve for eleve in liste_eleves if eleve[3] > 15]`",
        ],
        [3],
    ],
    [
"""
On dispose du dictionnaire suivant : `#!py tel = {'Bill': '06 05 04 03 02', 'Roger': '06 12 11 13 20'}`

Comment obtenir la liste des numéros de téléphones ?
""",
        [
            "`#!py list(tel.items())`",
            "`#!py list(tel)`",
            "`#!py list(tel.values())`",
            "`#!py list(tel.keys())`",
            "Autre réponse",
        ],
        [3],
    ],
    [
"""
On a :

```python title=''
animaux = ['Chat', 'Cochon', 'Chien', 'Canard', 'Vache']
effectif = [3, 8, 5, 9, 1]
groupe = [animaux, effectif]
```

Que vaut `#!py groupe[1][3]` ?
""",
        [
            "`#!py 9`",
            "`#!py 'Chien'`",
            "`#!py 'Canard'`",
            "`#!py 5`",
        ],
        [1],
    ],
    [
"""
Dans la déﬁnition suivante de la fonction `#!py somme` en Python, quelle est l’instruction à ajouter pour que la valeur renvoyée par l’appel `#!py somme([10 , 11 , 12 , 13 , 14])` soit 60 ?

```python title=''
def somme (tab):
   s = 0
   for ind in range(len(tab)):
      ...
   return s
```
""",
        [
            "`#!py s = s + tab[ind]`",
            "`#!py s = tab[ind]`",
            "`#!py s = s + ind`",
            "`#!py tab [ind] = tab[ind] + s`",
        ],
        [1],
    ],
    [
"""
Voici un dictionnaire de langues :
`#!py dico = {'anglais':'english', 'allemand':'deutsch', 'breton':'brezhoneg'}`

On souhaite ajouter une langue en plus et obtenir le dictionnaire suivant :
`#!py dico = {'anglais':'english', 'allemand':'deutsch', 'breton':'brezhoneg', 'espagnol':'español'`


Quelle instruction permet d'ajouter l'élément `#!py 'espagnol':'español'` dans le dictionnaire ?
""",
        [
            "`#!py dico.append('espagnol':'español')`",
            "`#!py dico['espagnol'] = 'español'`",
            "`#!py dico += ['espagnol':'español']`",
            "Ce n'est pas possible car un dictionnaire n'est pas modifiable",
        ],
        [2],
    ],
    [
"""
Que s'affiche-t-il si l'on exécute le script suivant ?

```python title=''
l = [0, 1, 2]
m = [3, 4, 5]
n = [l[i] + m[i] for i in range(len(l))]
print(n)
```
""",
        [
            "Erreur",
            "`#!py [3, 5, 7, 9]`",
            "`#!py [0, 1, 2, 3, 4, 5]`",
            "`#!py [3, 5, 7]`",
        ],
        [4],
    ],
    [
"""
Voici un extrait de la liste `#!py personnes`

```python title=''
personnes = [{'prénom': 'Marius', 'ville': 'Paris'},
             {'prénom': 'Nassim', 'ville': 'Angers'},
             {'prénom': 'Eléa', 'ville': 'Nantes'},
             ...
            ]
```

Quelles instructions permettent de donner la liste des prénoms des personnes nées à Rouen?
""",
        [
            "`#!py [p['prénom'] for p in personnes if p['ville'] == 'Rouen']`",
            "`#!py [personnes['prénom'] for p in personnes if personnes['ville'] == personnes['Rouen']]`",
            "`#!py [p['prénom'] for p in personnes if if p['ville'] == p['Rouen']]`",
            "`#!py [prénom for p in personnes if p['ville'] == 'Rouen']`",
            "Autre réponse",
        ],
        [1],
    ],
    [
"""
    Quelle expression permet d'accéder au numéro de Tournesol :
    ```python title=''
    repertoire = [{'nom': 'Dupont', 'tel': 5234}, {'nom': 'Tournesol', 'tel': 5248}, {'nom': 'Dupond', 'tel': 5237}]
    ```
""",
        [
            "`#!py repertoire[1]['tel']`",
            "`#!py repertoire['tel'][1]`",
            "`#!py repertoire['Tournesol']`",
            "`#!py repertoire['Tournesol']['tel']`",
        ],
        [1],
    ],
    [
"""
On considère la liste de p-uplets suivante :
```python title=''
table = [ ('Grace', 'Hopper', 'F', 1906),
('Tim', 'Berners-Lee', 'H', 1955),
('Ada', 'Lovelace', 'F', 1815),
('Alan', 'Turing', 'H', 1912) ]
```

où chaque p-uplet représente un informaticien ou une informaticienne célèbre ; le premier élément est son prénom, le deuxième élément son nom, le troisième élément son sexe (‘H’ pour un homme, ‘F’ pour une femme) et le quatrième élément son année de naissance (un nombre entier entre 1000 et 2000).

On définit une fonction :
```python title=''
def fonction_mystere(table):
    mystere = []
    for ligne in table:
        if ligne[2] == 'F':
            mystere.append(ligne[1])
    return mystere
```

Que vaut `#!py fonction_mystere(table)`?
""",
        [
            "`#!py ['Hopper', 'Lovelace']`",
            "`#!py []`",
            "`#!py [('Grace', 'Hopper', 'F', 1906), ('Ada', 'Lovelace', 'F', 1815)]`",
            "`#!py [‘Grace’, ‘Ada’]`",
            "Autre réponse",
        ],
        [1],
    ],
    [
"""
On donne ci-dessous le début du tableau `#!py personnes`
```python title=''
personnes = [{'prénom': 'Marius', 'ville': 'Paris', 'année': '2004'},
             {'prénom': 'Nassim', 'ville': 'Angers', 'année': '1972'},
             {'prénom': 'Eléa', 'ville': 'Nantes', 'année': '1993'},
             ...
            ]
```

Quelle instruction permet de construire un tableau t contenant les prénoms de toutes les personnes nées en 2001 ?
""",
        [
            "`#!py t = [if p['année'] == '2001': p['prénom']]`",
            "`#!py t = [personnes if p['année'] == '2001']`",
            "`#!py t = [p for p in personnes if p['année'] == '2001']`",
            "`#!py t = [p['prénom'] for p in personnes if p['année'] == '2001']`",
            "Autre réponse",
        ],
        [4],
    ],
    [
"""
La fonction suivante doit calculer la moyenne d'un tableau de nombres, passé en paramètre. Avec quelles expressions faut-il compléter l'écriture pour que la fonction soit correcte ?
```python title=''
def moyenne(tableau) :
     total = ...
     for valeur in tableau :
          total = total + valeur
     return total / .....
```
""",
        [
            "1 et `#!py len(tableau)`",
            "1 et `#!py len(tableau) + 1`",
            "0 et `#!py len(tableau)`",
            "0 et `#!py len(tableau) + 1`",
            "Autre réponse",
        ],
        [3],
    ],
    [
        "Quel type de serveur associe un nom de domaine avec une adresse IP ?",

        [
            "un serveur FTP",
            "un serveur HTTP",
            "un serveur Web",
            "un serveur DNS",
            "Autre réponse",
        ],
        [4],
    ],
    multi = False,
    qcm_title = "QCM de première",
    ID = 2,
    DEBUG = False,
    shuffle = True
) }}
