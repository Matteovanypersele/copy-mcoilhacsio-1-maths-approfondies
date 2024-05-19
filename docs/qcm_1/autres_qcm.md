---
author: Mireille
title: Essais de qcm
tags:
  - qcm
  - Difficulté **
---



## Multi QCM original ancien Pyodide


{{multi_qcm(
["Quelle est la réponse à la question universelle ? Cocher deux réponses.", 
["$6\\times 7$", "$\\int_0^{42} 1 dx$", "Je ne sais pas", " `#!py sum([i for i in range(10)])`", "La réponse D"], [1, 2]],
["1 + 1 = ? Cocher deux réponses.",
["Je ne sais pas", "2", "L'âge du capitaine", "10 en binaire"], [2, 4]]
)}}


## De Fred avec bug

multi_qcm(
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
        {'multi':True}
    ],
    multi = False,
    qcm_title = "Un QCM avec mélange automatique des questions (bouton en bas pour recommencer)",
    DEBUG = False,
    shuffle = True,
)



## De Fred autre essai

multi_qcm(
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
        {'multi':True}
    ],
    multi = False,
    qcm_title = "Un QCM avec mélange automatique des questions (bouton en bas pour recommencer)",
    DEBUG = False,
    shuffle = True,
)
