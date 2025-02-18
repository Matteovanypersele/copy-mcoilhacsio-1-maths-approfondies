---
author: Mireille Coilhac
title: Loi de Poisson
tags:
    - probabilités
---

## I. Présentation de la loi de Poisson

!!! example "Exemple"

    Supposons que nous gérions un centre d'appels qui reçoit en moyenne 5 appels par heure (en dehors des heures de pointe). Nous voulons connaître la probabilité de recevoir exactement 3 appels téléphoniques en une heure (en dehors des heures de pointe). 

    * Les événements (recevoir un appel) se produisent de manière indépendante. Le fait de recevoir un appel à un moment donné n'affecte pas la probabilité de recevoir un autre appel quelques minutes plus tard.

    * Les événements se produisent aussi de manière uniforme : cela signifie qu'à chaque minute de l'heure, la probabilité de recevoir un appel est la même. Il n'y a pas de moments particuliers où plus ou moins d'appels sont attendus.

!!! info "La loi de Poisson"

    ![Poisson](images/256px-Simeon_Poisson_(cropped).jpg){ width=20% }

    _Siméon Denis Poisson_

    La loi de Poisson est une loi de probabilité discrète qui modélise des phénomènes où les événements se produisent de manière indépendante et uniforme sur un intervalle de temps ou dans un espace donné.

    $$P(X=k) = \frac{\lambda^k \text{e}^{-\lambda}}{k!}$$

    où :

    * $X$ est une variable aléatoire représentant le nombre d'événements (par exemple, le nombre d'appels téléphoniques),
    * $k$ est le nombre spécifique d'événements que nous voulons calculer la probabilité,
    * $\lambda$ est le taux moyen d'événements par unité de temps (par exemple, le nombre moyen d'appels téléphoniques par heure).

    Cette formule **n'est pas à mémoriser**. On utilisera la **calculatrice** pour tout calcul de probabilité.

!!! example "Exemple"

    Supposons que nous gérions un centre d'appels qui reçoit en moyenne 5 appels par heure en dehors des heures de pointe. Nous voulons connaître la probabilité de recevoir exactement 3 appels téléphoniques en une heure.

    Dans cet exemple :

    * $\lambda = 5$ (le taux moyen d'appels par heure),

    * $k = 3$ (le nombre d'appels que nous voulons calculer).

    Appliquons la formule de la loi de Poisson : $P(X=3) = \frac{\lambda^3 \text{e}^{-\lambda}}{3!}$

    Grâce à la calculatrice on trouve : $P(X=3) \approx 0.1404$

## II. Propriétés de la loi de Poisson

!!! info "À retenir"

    Si $X$ est une variable aléatoire qui suit la loi de Poisson de paramètre $\lambda$ alors :

	* $E(X)=\lambda$
	* $V(X)=\lambda$
	* $\sigma(X)=\sqrt{\lambda}$

!!! abstract "Le paramètre $\lambda$"

    Le paramètre $\lambda$ est la moyenne des valeurs de la variable aléatoire X : $\lambda$ est le nombre moyen de fois que l'événement considéré (le succès) a été réalisé pendant  l'intervalle de temps étudié ou bien dans l'espace étudié.
 


## III. Visualiser la loi de Poisson

[La loi de Poisson sur GeoGebra](https://www.geogebra.org/m/fJES3J22){ .md-button target="_blank" rel="noopener" }

## IV. Calculatrices et loi de Poisson

[Calculatrice Numworks](https://www.numworks.com/fr/manuel/probabilites/){ .md-button target="_blank" rel="noopener" }
[Calculatrice CASIO](https://www.casio-education.fr/wp-content/uploads/2024/01/menu_probabilites_graph-light.pdf?x23188){ .md-button target="_blank" rel="noopener" }
[Calculatrice TI](a_telecharger/ProbabilitsloidePoisson.pdf){ .md-button target="_blank" rel="noopener" }

## V. Approximation d'une loi binomiale par une loi de Poisson

!!! info "Approximation"

    On peut montrer que la loi de Poisson est une approximation de la loi binomiale dans le cas où la probabilité du succès (ou de l'échec) est très faible et le nombre de tirages important.

    Si $n$ est "très grand" , $p$ "voisin de 0" et $np$ "pas trop grand" \fg", alors la loi binomiale $\mathcal{B}(n, p)$ est très proche de la loi de poisson de paramères $\lambda$ où $\lambda=np$. Il y a conservation de l'espérance mathématique.

    On convient en général d'utiliser cette approximation lorsque $n \pg 30$,   $p \pp 0,1$ et $np<15$  ou lorsque $n \pg 50$, $p \pp 0,1$ et $np \pp 10$ (Ces conditions ne sont pas à mémoriser).

## VI. Exercices

## VII Crédits

Cédic Pierquet





