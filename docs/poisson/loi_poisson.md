---
author: Mireille Coilhac
title: Loi de Poisson
tags:
    - probabilités
---

## Présentation de la loi de Poisson

!!! example "Exemple"

    Supposons que nous gérions un centre d'appels qui reçoit en moyenne 5 appels par heure (en dehors des heures de pointe). Nous voulons connaître la probabilité de recevoir exactement 3 appels téléphoniques en une heure (en dehors des heures de pointe). 

    * Les événements (recevoir un appel) se produisent de manière indépendante. Le fait de recevoir un appel à un moment donné n'affecte pas la probabilité de recevoir un autre appel quelques minutes plus tard.

    * Les événements se produisent aussi de manière uniforme : cela signifie qu'à chaque minute de l'heure, la probabilité de recevoir un appel est la même. Il n'y a pas de moments particuliers où plus ou moins d'appels sont attendus.

!!! info "La loi de Poisson"

    La loi de Poisson est une loi de probabilité discrète qui modélise des phénomènes où les événements se produisent de manière indépendante et uniforme sur un intervalle de temps ou dans un espace donné.

    <a href="https://commons.wikimedia.org/wiki/File:Simeon_Poisson_(cropped).jpg">François-Séraphin Delpech</a>, Public domain, via Wikimedia Commons

    _Siméon Denis Poisson_

    $$P(X=k) = \frac{\lambda^k \text{e}^{-\lambda}}{k!}$$

    où :

    $X$ est une variable aléatoire représentant le nombre d'événements (par exemple, le nombre d'appels téléphoniques),

    $k$ est le nombre spécifique d'événements que nous voulons calculer la probabilité,

    $\lambda$ est le taux moyen d'événements par unité de temps (par exemple, le nombre moyen d'appels téléphoniques par heure).

    Cette formule **n'est pas à mémoriser**. On utilisera la **calculatrice** pour tout calcul de probabilité.

!!! example "Exemple"

    Supposons que nous gérions un centre d'appels qui reçoit en moyenne 5 appels par heure en dehors des heures de pointe. Nous voulons connaître la probabilité de recevoir exactement 3 appels téléphoniques en une heure.

    Dans cet exemple :

    * $\lambda = 5$ (le taux moyen d'appels par heure),

    * $k = 3$ (le nombre d'appels que nous voulons calculer).

    Appliquons la formule de la loi de Poisson : $P(X=3) = \frac{\lambda^3 \text{e}^{-\lambda}}{3!}$

    Grâce à la calculatrice on trouve : $P(X=3) \approx 0.1404$




