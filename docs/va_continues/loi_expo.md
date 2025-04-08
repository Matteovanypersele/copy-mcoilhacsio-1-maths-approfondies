---
author: Mireille Coilhac
title: Loi exponentielle
tags:
    - variables aléatoires
---

À venir ...

## Exercices

### D'après BTS SIO Polynésie mai 2019

???+ question "Exercice 1 partie D"

    La durée de vie, en mois, d'un composant, peut être modélisée par une variable aléatoire $T$ qui suit 
    une loi exponentielle de paramètre $\lambda$.

    **1** Exprimer en fonction de $\lambda$ la probabilité $P(T \geqslant t)$.

    ??? success "Solution"

        $R(t)=\text{e}^{- \lambda t}$. On a donc $P(T \geqslant t) = \text{e}^{- \lambda t}$

    **2** Sachant que $P(T > 24) = 0,698$, calculer $\lambda$ en arrondissant la valeur au millième.

    ??? success "Solution"

        Il faut donc résoudre $\text{e}^{- 24 \times \lambda}= 0,698$. Cela équivaut à :   
        $-24 \times \lambda = \text{ln} (0,698)$   
        $\Leftrightarrow \lambda = \dfrac{\text{ln} (0,698)}{-24}$  
        $\Leftrightarrow \lambda = \approx 0,015$  à $10^{-3}$ près.

    **3. a)** Dans cette question on prendra $\lambda = 0,015$.  
    Déterminer l'espérance mathématique de la variable $T$, arrondie à l'unité.

    ??? success "Solution"

        l'espérance mathématique de la variable $T$ est égale à $E(T) = \dfrac{1}{\lambda}$  
        On a donc $E(T) = \dfrac{1}{0,015} \approx 67$ arrondi à l'unité.

    **3. b)** Calculer la probabilité que le composant fonctionne encore au bout de 3 ans.

    ??? success "Solution"

        3 ans correspond à 36 mois. $P(T \geqslant 36)= \text{e}^{- 36 \times 0,015 \approx 0,58} à $10^{-2}$ près

