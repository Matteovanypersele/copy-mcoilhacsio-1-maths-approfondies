---
author: Mireille
title: Ecrire des QCM
tags:
  - qcm
  - Difficulté **
---



## Multi QCM ancien Pyodide


{{multi_qcm(
["Quelle est la réponse à la question universelle ? Cocher deux réponses.", 
["$6\\times 7$", "$\\int_0^{42} 1 dx$", "Je ne sais pas", " `#!py sum([i for i in range(10)])`", "La réponse D"], [1, 2]],
["1 + 1 = ? Cocher deux réponses.",
["Je ne sais pas", "2", "L'âge du capitaine", "10 en binaire"], [2, 4]]
)}}




## QCM avec des questions sur plusieurs lignes

{{ multi_qcm(
    [
"""
On a saisi le code suivant :
```python title=''
n = 8
while n > 1:
    n = n/2
```

Que vaut `n` après l'exécution du code ?
""",
        [
            "2.0",
            "4.0",
            "1.0",
            "0.5",
        ],
        [3]
    ],
    [
        "Quelle est la machine qui va exécuter un programme JavaScript inclus dans une page HTML ?",
        [
            "La machine de l’utilisateur sur laquelle s’exécute le navigateur web.",
            "La machine de l’utilisateur ou du serveur, selon celle qui est la plus disponible.",
            "La machine de l’utilisateur ou du serveur, suivant la conﬁdentialité des données manipulées.",
            "Le serveur web sur lequel est stockée la page HTML."
        ],
        [1],
    ],
    [
"""
Cocher toutes les bonnes réponses
```python title=''
meubles = ['Table', 'Commode', 'Armoire', 'Placard', 'Buffet']
```
""",
        [
            "`#!py meubles[1]` vaut `#!py Table`",
            "`#!py meubles[1]` vaut `#!py Commode`",
            "`#!py meubles[4]` vaut `#!py Buffet`",
            "`#!py meubles[5]` vaut `#!py Buffet`",
        ],
        [2, 3],
        {'multi':True}
    ],
    multi = False,
    qcm_title = "Un QCM avec mélange automatique des questions (bouton en bas pour recommencer)",
    DEBUG = False,
    shuffle = True,
) }}
