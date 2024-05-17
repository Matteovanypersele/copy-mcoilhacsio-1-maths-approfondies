---
author: Nicolas Revéret
hide:
    - navigation
    - toc
title: Arbre binaire additif
difficulty: 350
tags:
    - tuple
    - arbre binaire
    - file
maj: 01/03/2024
---

On souhaite construire des arbres binaires parfaits « *additifs* ». Dans ces arbres :

* tous les niveaux sont entièrement remplis ;
* la valeur d'un nœud intérieur est toujours égale à la somme des valeurs de ses enfants.

???+ example "Un exemple d'arbre binaire *additif*"

    <center>
    ```mermaid
    graph TD
        R(19) --> A(8)
        R --> B(11)
        A --> C(3)
        A --> D(5)
        B --> E(7)
        B --> F(4)
        C -.-x G( )
        C -.-x H( )
        D -.-x I( )
        D -.-x J( )
        E -.-x K( )
        E -.-x L( )
        F -.-x M( )
        F -.-x N( )
        style G display:none;
        style H display:none;
        style I display:none;
        style J display:none;
        style K display:none;
        style L display:none;
        style M display:none;
        style N display:none;
    ```
    </center>
    
    Cet arbre est :
    
    * parfait (tous ses niveaux sont remplis) ;
    
    * *additif* (on a $3 + 5 = 8$ ; $7 + 4 = 11$ ; $8 + 11 = 19$).
    

On demande d'écrire la fonction `arbre_additif` qui prend en argument la liste `valeurs` contenant les valeurs des feuilles et renvoie l'arbre correspondant représenté à l'aide de tuples.

On garantit que le nombre d'éléments de `valeurs` est une puissance de $2$ strictement positive. Ces éléments sont tous des nombres entiers.


???+ note "Représentation des arbres en machine"

    On représente les arbres binaires ainsi :

    - l'arbre vide est représenté par `#!py None`,

    - un arbre non vide est représenté par un tuple `(sous-arbre gauche, valeur, sous-arbre droit)`.

    Ainsi le tuple `((None, 6, None), 15, None)` représente l'arbre suivant :

    <center>
    ```mermaid
    graph TD
        R(15) --> A(6)
        R -.-x B( )
        A -.-x C( )
        A -.-x D( )
        style B display:none;
        style C display:none;
        style D display:none;
    ```
    </center>

???+ example "Exemples"

    ```pycon title=""
    >>> arbre_additif([6])
    (None, 6, None)
    >>> arbre_additif([6, 9])
    ((None, 6, None), 15, (None, 9, None))
    >>> arbre_additif([3, 5, 7, 4])
    (((None, 3, None), 8, (None, 5, None)), 19, ((None, 7, None), 11, (None, 4, None)))
    ```

??? tip "Parcours possible"

    L'algorithme peut être construit autour d'un parcours en largeur partant du dernier niveau de l'arbre (les feuilles) et remontant, niveau par niveau, jusqu'à la racine.
    

??? tip "Avec deux `#!py list`..."
    
    On peut, par exemple, débuter en construisant une liste contenant les feuilles. On calcule ensuite la liste contenant les nœuds du niveau supérieur.
    
    Ce calcul effectué, on remplace la liste des nœuds par la nouvelle et on répète la démarche jusqu'à atteindre la racine.

??? tip "... ou avec une `file`"
        
    On pourra aussi utiliser une structure de file afin de mettre œuvre un parcours en largeur « remontant » l'arbre.
    
    On fournit à ce titre les fonctions `creer_file`, `enfiler` et `defiler` d'ores et déjà chargées en mémoire et **utilisables sans effectuer d'imports**.

    ```pycon
    >>> f = creer_file()  # création d'une file vide
    >>> enfiler(f, 0)     # on enfile la valeur 0 dans f
    >>> enfiler(f, 1)     # on enfile la valeur 1 dans f
    >>> enfiler(f, 2)     # on enfile la valeur 2 dans f
    >>> defiler(f)        # on défile, et l'on récupère, une valeur de f
    0
    >>> defiler(f)        # on défile, et l'on récupère, une valeur de f
    1
    >>> defiler(f)        # on défile, et l'on récupère, une valeur de f
    2
    >>> len(f)            # nombre d'éléments dans f
    0
    ```

{{ IDE('exo') }}
