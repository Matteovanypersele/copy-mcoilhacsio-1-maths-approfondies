---
author: Mireille Coilhac
title: Variables aléatoires contines - introduction
tags:
    - variables aléatoires
---

## Loi uniforme

!!! info "Loi uniforme"

    La loi uniforme sur un intervalle est la version continue d'équiprobabilité dans le cas d'un nombre fini d'issues.

!!! example "Exemple"

    Voici l'histogramme des fréquenes pour un échantillon de taille $10 000$ d'une varable aléatoire $X$ suivant une loi uniforme sur l'intervalle $[0; 4]$ (Cela signifie que $X$ peut prendre comme valeurs tous les réels de $[0; 4]$)

    ![nom image](images/intro_loi_unif.png){ width=30% }

    L'axe des ordonnée est gradué de façon à ce que l'aire de chaque rectangle soit égale à la probabilité de la classe (c'et-à-dire de l'intervalle) correspondante.

    On lit donc $P(0,8<X<1,2)=0,25 \times(1,2 - 0,8)=0,25 \times 0,4 = 0,1$

    Déterminer $P(0,8<X<1,6)$

    ??? success "Solution"

        D'après l'histogramme : $P(0,8<X<1,6) = 0,25 \times(1,6 - 0,8)=0,25 \times 0,8 = 0,2$

???+ question "Loi uniforme sur $[0; 4]$"

    $X$ suit une loi uniforme sur $[0; 4]$ si tous les intervalles de même amplitude inclus dans [0 ;4]  ont la même probabilité d’être obtenus.

    $X$ peut prendre comme valeurs tous les réels de $[0; 4]$ et aucune autre.

    On a donc $P(0<X<4)=1$

    $P(0<X<2)= P(2<X<4)$ et $P(0<X<2) + P(2<X<4) = 1$

    On a donc $P(0<X<2)= P(2<X<4) = \dfrac{1}{2}$



    


