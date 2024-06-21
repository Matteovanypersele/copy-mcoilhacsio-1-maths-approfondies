---
author: Mireille Coilhac
title: Statistiques à une variable
tags:
    - statistiques
---

## I. Définitions et notations

!!! info "Caractères quantitatifs à valeurs discrètes ou continues"

    Dans ce chapitre, on étudie des séries à caractères **quantitatifs discrètes** (à valeurs séparées) ou **continues** 
    (dont les valeurs sont regroupées en classes, ou intervalles).  
    Dans le cas d’une série continue, on fait toujours l’hypothèse que la répartition des valeurs est uniforme à 
    l’intérieur de chaque classe.

!!! info "Notations"

	* $X$ est le caractère étudié et $x_1$, $x_2$, ..., $x_p$ les **valeurs** du caractère ou les centres des 
    classes dans le cas où les valeurs sont regroupées en classes. Ces valeurs sont **rangées dans l’ordre croissant**.
	* $n_1$, $n_2$, ..., $n_p$ sont les **effectifs** respectifs des valeurs $x_1$, $x_2$, ..., $x_p$.
	* $f_1$, $f_2$, ..., $f_p$ sont les **fréquences** respectives des valeurs $x_1$, $x_2$, ..., $x_p$.
	* $N$ est l’effectif total, et $N=n_1+n_2+...+n_p$

!!! info "Fréquences"

    * La fréquence de la valeur $x_i$ est donnée par $f_i=\dfrac{n_i}{N}$.

    * Ce nombre est compris dans  l’intervalle $[0;1]$ et est souvent écrit sous la forme d’un pourcentage.

    La somme de toutes les fréquences est égale à 1 : $\sum_{i=1}^p f_i=f_1+f_2+...+f_p=1$.

!!! info "Effectif cumulé, fréquence cumulée pour une série discreète"

    C'est le nombre d'individus pour lesquels la valeur du caractère est **inférieure ou égale** à $x_i$.

    On a $S_i= n_1+n_2+...+n_i$ et de ce fait on a $S_p  = N$ (dernier effectif cumulé).

    La fréquence cumulée en $x_i$ est donnée par $F_i=f_1+f_2+...+f_i=\dfrac{S_i}{N}.$


!!! info "Effectif cumulé, fréquence cumulée pour une série continue"

    Pour l'effectif cumulé d'une classe $]a;b]$, il s'agit de l'effectif cumulé en $b$ (borne droite de 
    l'intervalle), c'est-à-dire le nombre d'individus pour lesquels la valeur du caractère est inférieure ou égale à $b$. 

    Ainsi, lorsqu'on calcule des effectifs cumulés pour une série statistique groupée en classes, ces effectifs 
    cumulés doivent être **impérativement** affectés aux **bornes de droite** de ces classes.

    Pour des raisons pratique, on fait l'hypothèse **répartition uniforme** à l'intérieur de chaque classe, 
    c'est-à-dire qu'il y a **proportionnalité entre les effectifs et les largeurs**.


## II. Paramètres de positions

!!! info "Médiane"

    La valeur médiane d’une série statistique est la valeur M séparant la population en deux moitiés : les 50 % 
    ayant une valeur inférieure ou égale à M et les 50 % ayant une valeur supérieure ou égale à M.

!!! info "Déterminer la médiane d'une série discrète"

    * Si l’effectif est impair, la médiane est la valeur de rang $\ndfrac{(N+1)}{2}$ 
    * si l’effectif est pair, la médiane est la moyenne des valeurs de rang $\dfrac{N}{2}$ et $\dfrac{N}{2}+1$.

!!! info "Déterminer la médiane d'une série continue"

    La médiane est la valeur correspondant à la fréquence cumulée égale à 0,5.

!!! info "Quartiles"

    * Le premier quartile est la valeur $Q_1$ telle que 25% de la population a une valeur du caractère inférieure 
    ou égale à $Q_1$, les 75% restants ayant une valeur supérieur ou égale à $Q_1$.

    * Le troisième quartile est la valeur $Q_3$ telle que 75% de la population a une valeur du caractère inférieure ou égale à $Q_3$, les 25% restants ayant une valeur supérieur ou égale à $Q_3$.

!!! info "Déterminer les quartiles d'une série discrète"

    * Si $\dfrac{N}{4}$ est un entier, $Q_1$ est la valeur de rang $\dfrac{N}{4}$ et $Q_3$ est la valeur de 
    rang $\dfrac{3N}{4}$.

    * Si $\dfrac{N}{4}$ n’est pas un entier, $Q_1$ est est la valeur de rang immédiatement supérieur
     à $\dfrac{N}{4}$ et $Q_3$ est la valeur de rang immédiatement supérieur à $\dfrac{3N}{4}$.

!!! info "Déterminer les quartiles d'une série continue"

    * $Q_1$ est la valeur correspondant à la fréquence cumulée égal à $0,25$
    * $Q_3$ est la valeur correspondant  à la fréquence cumulée égale à $0,75$.

!!! info "Intervalle intequartile et écart interquartile"

    * Intervalle interquartile : c’est l’intervalle $[Q_1;Q_3]$.

    * Écart interquartile : c’est la valeur de $Q_3-Q_1$. 

!!! info "Moyenne"

    * Pour une série **discrète**, la moyenne des valeurs $x_1$, $x_2$, ..., $x_p$ 
    d'effectifs $n_1$, $n_2$, ..., $n_p$  (effectif total N) est le réel : 
    $$\bar{x}=\dfrac{n_1 x_1+n_2 x_2+...+n_p x_p}{n_1+n_2+...+n_p}=\dfrac{1}{N} \sum_{i=1}^p n_i x_i.$$

    * Pour une série **continue**, on applique la même formule en prenant pour les valeurs $x_i$ les centres des classes.


## III. Paramètres de dispersion :

!!! info "Mesurer la dispersion"

    La moyenne d'un caractère statistique ne suffit pas pour caractériser le comportement de ses valeurs.

    Par exemple, les étudiants d'un premier groupe peuvent avoir obtenu des résultats très homogènes (c'est-à-dire 
    des notes comprises dans un petit intervalle autour de 10) alors que ceux d'un deuxième groupe peuvent avoir 
    des résultats beaucoup plus dispersés autour de 10. L'**écart-type** est un nombre qui mesure de cette **dispersion**, 
    au sens où plus l'écart-type est élevé plus les valeurs sont dispersées autour de la moyenne.

!!! info "Variance et écart-type"

    La **variance d’une série statistique de caractère X prenant les valeurs (ou centres des classes) 
    $x_1$, $x_2$, ..., $x_p$ d’effectifs respectifs $n_1$, $n_2$, ..., $n_p$ et de moyenne $\overline{x}$ 
    est le nombre $$V(x)=\dfrac{1}{N} \sum_{i=1}^p \left(x_i-\bar{x}\right)^2=\dfrac{1}{N} \sum_{i=1}^p n_i x_i^2 - \overline{x}^2.$$%

    On en déduit l'**écart-type** de la série $\sigma(X)=\sqrt{V(X)}$ qui est toujours un nombre positif.






   


   


   

## IV. Usage de la calculatrice

!!! info "Différentes calculatrices"

    [CASIO](a_telecharger/100_graph35_E_2015_VF.pdf){ .md-button target="_blank" rel="noopener" }

    [Numworks](a_telecharger/100_NumWorks.pdf){ .md-button target="_blank" rel="noopener" }

    [Texas TI 82](a_telecharger/100_ti82advanced_VF.pdf){ .md-button target="_blank" rel="noopener" }

    [Texas TI 83](a_telecharger/100_ti83PremiumCE_version_finale.pdf){ .md-button target="_blank" rel="noopener" }



## V. Exercices

[Exercices sur les statistiques à une variable](https://coopmaths.fr/alea/?uuid=crpe-2017-g5-ex3&uuid=crpe-2015-g2-ex3&uuid=crpe-2017-g2-ex1&uuid=crpe-2016-pol-ex4&uuid=crpe-2019-g2-ex4&uuid=crpe-2016-cre-ex2&uuid=crpe-2019-g5-ex1&uuid=crpe-2019-g5-ex1&uuid=crpe-2016-g2-ex1&uuid=b7662&id=2S20-5&n=2&d=10&s=1&cd=1&v=eleve&es=0111001&title=){ .md-button target="_blank" rel="noopener" }

## Crédits

Source pour le I II et III : Cédric Pierquet