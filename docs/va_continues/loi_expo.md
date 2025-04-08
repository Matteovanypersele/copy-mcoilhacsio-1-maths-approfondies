---
author: Mireille Coilhac
title: Loi exponentielle
tags:
    - variables aléatoires
---

## I. Durée de vie et loi exponentielle

!!! info "Durée de vie"

    La durée de vie d'un matériel donné sera modélisée par une variable aléatoire continue $T$ prenant (théoriquement) ses valeurs dans l'intervalle $[0; +\infty]$. Pour une valeur $t$ dans cet intervalle on utilise les notations suivantes :
    * $F(t) = p(T \pp t)$ 
	* $R(t) = 1 - F(t) = p(T > t)$

    👉 La probabilité $F(t) = p(T \pp t)$ s'interprète comme la probabilité que le matériel connaisse une défaillance avant l'instant $t$ : pour cette raison F est appelée la **fonction de défaillance** du matériel (en anglais, défaillance se dit \textit{failure}, d'où la lettre F).  
    💡Pour vous souvenir de **$F$** vous pouvez penser à "Faute"

    👉 Inversement, la probabilité $R(t) = p(T > t)$ s'interprète comme la probabilité que le matériel ait fonctionné correctement jusqu'à l'instant $t$ : R est donc appelée **fonction de fiabilité** du matériel (en anglais, fiabilité se dit \textit{reliability}, d'où la lettre R).  
    💡Pour vous souvenir de **$R$** vous pouvez penser à "Réussite"

!!! info "Loi exponentielle"

    La variable aléatoire $T$ (la durée de vie du matériel) suit une **loi exponentielle** de paramètre $\lambda$ loorsque la fonction de fiabilité R s'écrit $R(t) = \e^{-\lambda t}$ où $\lambda$ est un réel **strictement positif**.  

    On a donc alors $p(T > t) = $P(T \geqslant t) = \text{e}^{- \lambda t}$

???+ question "À vous de jouer 1"

    On prélève au hasard une ampoule dans un lot et on admet que sa durée de vie définit une variable aléatoire $T$ qui suit une loi exponentielle de paramètre $\lambda=0,0005$.

    **1** Déterminer la probabilité de l'événement A : « l'ampoule fonctionne correctement au bout de 1 000 heures »

    ??? success "Solution"

        $p(A) = P(T>1000) = \e^{-0,0005 \times 1000}=\e^{-0,5} \approx 0,6065$

    **2** Déterminer la probabilité de l'événement B : « l'ampoule fonctionne correctement au bout de 1 500 heures »

    ??? success "Solution"

        $p(B) = P(T>1500) = \e^{-0,0005 \times 1500}=\e^{-0,75} \approx 0,4724$

    **3.** Déterminer la probabilité de l'événement C : « l'ampoule fonctionne correctement au bout de 500 heures »

    ??? success "Solution"

        $p(B) = P(T>500) = \e^{-0,0005 \times 500}=\e^{-0,25} \approx 7788$

    
    **4.** Déterminer la probabilité de l'événement D : « l'ampoule fonctionne correctement au bout de 1500 heures sachant qu'elle a fonctionné correctement 1000 heures"

    ??? success "Solution"   

        $p_A (B) =  \dfrac{p(A \cap B)}{p(A)}=\dfrac{p(B)}{p(A)}=\dfrac{\e^{-0,75}}{\e^{-0,5}} = \e^{-0,25}$ **qui est exactement** p(C)$.



!!! info "La loi exponentielle est une loi sans sans vieillissement"

    L'exemple précédant nous montre que la probabiliténde bon fonctionnement pendant 1500 heures sachant qu'on a eu un bon fonctionnement pendant 1000 heures est tout simplement la même que la probabilité de bon fonctionnement pendant $1500 - 1000 = 500$ heures.

    Une loi exponentielle modélise la durée de vie d’un phénomène **sans mémoire**, ou **sans vieillissement**, ou sans usure : le fait que le phénomène ait duré pendant t heures ne change rien à son espérance de vie à partir du temps t.

    Cette loi permet entre autres de modéliser la durée de vie de la radioactivité ou d’un composant électronique.


!!! info "Conséquence"

    Ainsi, la probabilité que le dispositif fonctionne encore correctement à la date $t_1  + t_2$  sachant qu'il a déjà fonctionné correctement  jusqu'à la date $t_1$, est exactement égale à la probabilité que le dispositif fonctionne encore correctement à la date $t_2$ (donc, a priori, comme si le dispositif avait fonctionné jusqu'à la date $t_2$ en étant « neuf » au départ).

    $p_{(T > t_1)}(T > t_1+t_2)=p(T >t_2 )$

## II. Espérence et écart type d'une variable aléatoire suivant une loi exponentielle de paramètre $\lambda$

!!! info "Par ❤️"

    Si une variable aléatoire $T$ suit une loi exponentielle de paramètre $\lambda$ alors : 

    * Son espérance est $E(T)= \dfrac{1}{\lambda}$
    * Son écart type est $\sigma (T) = \dfrac{1}{\lambda}$

    👉 $E(T)$ s'appelle le **MTBF** (Moyenne des Temps de Bon Fonctionnement)

    $\text{MTBF}= \dfrac{1}{\lambda}$

!!! info "Méthode"

    Parfois dans un exercice $\lambda$ n'est pas donné. Dans ce cas-là on peut le retrouver si : 

    * on nous donne le MTBF
    * on nous donne une probabilité particulière. Il suffit alors de résoudre une équation (penser à utiliser la fonction ln)



## III. Exercices

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
        $\Leftrightarrow \lambda  \approx 0,015$  à $10^{-3}$ près.

    **3. a)** Dans cette question on prendra $\lambda = 0,015$.  
    Déterminer l'espérance mathématique de la variable $T$, arrondie à l'unité.

    ??? success "Solution"

        L'espérance mathématique de la variable $T$ est égale à $E(T) = \dfrac{1}{\lambda}$  
        On a donc $E(T) = \dfrac{1}{0,015} \approx 67$ mois arrondi à l'unité.

    **3. b)** Calculer la probabilité que le composant fonctionne encore au bout de 3 ans.

    ??? success "Solution"

        3 ans correspond à 36 mois. $P(T \geqslant 36)= \text{e}^{- 36 \times 0,015} \approx 0,58$ à $10^{-2}$ près

