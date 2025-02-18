---
author: Mireille Coilhac
title: Loi de Poisson
tags:
    - probabilités
---

## Prérequis

[Variables aléatoires discrètes](https://mcoilhac.forge.apps.education.fr/sio-1-maths-approfondies/var_aleat/variables_aleatoires/){ .md-button target="_blank" rel="noopener" }

[Loi binomiale](https://mcoilhac.forge.apps.education.fr/sio-1-maths-approfondies/loi_binomiale/binomiale/){ .md-button target="_blank" rel="noopener" }

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

    Si $n$ est "très grand" , $p$ "voisin de 0" et $np$ "pas trop grand" , alors la loi binomiale $\mathcal{B}(n, p)$ est très proche de la loi de poisson de paramères $\lambda$ où $\lambda=np$. Il y a conservation de l'espérance mathématique.

    On convient en général d'utiliser cette approximation lorsque $n \geq 30$,   $p \leq 0,1$ et $np<15$  ou lorsque $n \geq 50$, $p \leq 0,1$ et $np \leq 10$ (Ces conditions ne sont pas à mémoriser).

## VI. Exercices

???+ question "Exercice 1"

    Les appareils sont conditionnés par lots de 100 pour l’expédition auxd istributeurs de pièces détachées. On prélève au hasard un échantillon de 100 appareils dans laproduction d’unejournée.La production est suffisamment importante pour quel ’onassimile ce pélèvement à un tirage avec remise de 100 appareils. Pour cette partie, onconsidère que, à chaque prélèvement, la probabilité que l’appareil soit défectueux est 0,05. On considère la variable aléaatoire $X$ qui, à tout prélèvement de 100 appareils, associe le nombre d’appareils défectueux. 
    
    **1 a)** Justifier que la variable aléatoire $X1$ suit une loi binomiale dont on précisera les paramètres. 

    ??? success "Solution"

        On répète 100 fois l’expérience de Bernoulli (l’appareil est d´efectueux ou pas), de manière indépendante. Le nombre $X$ d’appareils défectueux suit donc une loi binomiale de paramètres $n = 100$ et $p = 0,05$.

    **1 b)** Donner l’espérance mathématique de la variable aléatoire $X$


    ??? success "Solution"

        L'espérance mathématique de la variable aléatoire $X$ est $E(X)=np=100 \times 0,05=5$

    **2.** On suppose que l’on peut approcher la loi de $X$ par une loi de Poisson de paramètre $\lambda$.
    **a)** Déterminer le paramètre $\lambda$.

    ??? success "Solution"

        On choisit $\lambda = 5$ puisque l’espérance $\lambda$ de la loi de Poisson doit être égale à l’espérance de la loi binomiale.

    **b)** En utilisant cette loi de Poisson, calculer la probabilité qu’il y ait au plus deux appareils défectueux dans un lot.

    ??? success "Solution"

        En utilisant la calculatrice on obtient $P(X \leq 2) \approx 0,125$


???+ question "Exercice 2"

    Une centrale téléphonique reçoit des appels à raison de 10 appels par heure en moyenne. On suppose que le nombre d’appels pendant un intervalle de temps quelconque suit une loi de Poisson. 
    
    **1.** Trouver la probabilité que durant deux minutes la centrale reçoive exactement trois appels. 

    ??? success "Solution"

        Le nombre moyen d’appels en deux minutes est $\lambda = \dfrac {20}{60}  = \dfrac{1} {3}$ . 
        
        La probabilité que durant deux minutes la centrale reçoive exactement trois appels est $P(X=3)=0,0044$
    
    
    **2.** Trouver la probabilité pour qu’en deux minutes, la centrale reçoive au moins un appel. 
    
    ??? success "Solution"

        $P(X \geq 1) = 1 - P(X = 0) _approx 0,283$


    
    **3.** Trouver la probabilité pour qu’en deux minutes, la centrale reçoive au moins trois appels.

    ??? success "Solution"

        $P(X \geq 3) = 1 - P(X \leq 2) _approx 0,005$

???+ question "Exerccie 3"

    Dans cet exercice, les valeurs approchées sont à arrondir à $10^{−2}$. Une entreprise fabrique en grande quantité des tiges en plastique de longueur théorique 100 mm. Dans un lot de ce type de tiges, 2% des tiges n’ont pas une longueur conforme. On prélève au hasard $n$ tiges de ce lot pour vérification de longueur. Le lot est assez important pour que l’on puisse assimiler ce prélèvement à un tirage avec remise de $n$ tiges. On considère la variable aléatoire X qui, à tout prélèvement de n tiges, associe le nombre de tiges de longueur non conforme de ce prélèvement.

    **1.** Pour cette question on prend $n = 50$.   
    **a)** Justifier que la variable aléatoire $X$ suit une loi binomiale dont on donnera les paramètres. 

    ??? success "Solution"

        On répète 50 fois l’expérience de Bernoulli (la tige est non conforme avec une probabilité 0,02 ou pas), de manière indépendante. Le nombre $X$ de tiges non conformes suit donc une loi binomiale de paramètres $n = 50$ et $p = 0,02$.
    
    **b)** Calculer $P(X = 3)$.

    ??? success "Solution"

        $P(X=3)=\binom{50}{3} (0.02)^3 (0.98)^47 \approx 0,06$

    **2.** Pour cette question, on prend $n = 100$. La variable aléatoire $X$ suit une loi binomiale que l’on d´ecide d’approcher par une loi de Poisson.  
    **a)** Déterminer le paramètre $\lambda$ de cette loi de Poisson.

    ??? success "Solution"

        On choisit $\lambda = 100 \times 0,002 = 2$ puisque l’espérance $\lambda$ de la loi de Poisson doit être égale à l’espérance de la loi binomiale.

    **b)** On désigne par $Y$ une variable aléatoire suivant la loi de Poisson de paramètre $\lambda$ où $\lambda$ est la paramètre obtenu à la question **2.a)**. À l’aide de l’approximation de $X$ par $Y$, calculer la probabilité d’avoir au plus 4 tiges de longueur non conforme.

    ??? success "Solution"

        Grâce à la calculatrice on trouve $P(Y \leq 4) \approx 0,95$

    

    
## VII Crédits

Cédric Pierquet et Pierrick Vaire





