---
author: Mireille Coilhac
title: Exercices - statistiques à deux variables
tags:
    - statistiques
---

## Exercice 1

???+ question "Exercice 1"

    Lors d'une enquête réalisée auprès de 500 personnes, on a estimé le nombre de personnes prêtes à acheter un nouveau produit en fonction du prix de ce produit :

    Prix proposé en euros ($x_i$) | 52 | 47 | 44 | $38,5$ | $35,5$ | 32 | 31 | 28 |
    |:---|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
	Nombre d'acheteurs potentiels ($y_i$) | 80 | 125 | 145 | 200 | 225 | 250 | 265 | 280|

    **1.** Question 1  
    Représenter **à la main sur votre feuille** le nuage de points $(x_i;y_i)$ en prenant 1 cm pour 5 euros en abscisse (de 15 à 60) et 1 cm pour 50 personnes en ordonnée (de 0 à 400).

    ??? success "Solution"

        ![corr_exo_1_doubles](images/graphe_exo_1_doubles.png){ width=50% }

    **2.** Question 2  
    Déterminer l'équation de la droite de régression de $y$ en $x$ sous la forme $y = ax + b$ en arrondissant $a$ à 2 décimales et $b$ à l'entier, ainsi que le coefficient de corrélation associé arrondi à 4 décimales.
	
	Cet ajustement linéaire vous parait-il raisonnable ?

    ??? success "Solution"

        La calculatrice nous donne $y=-8,53x+525$ et $r \approx -0,9986$ qui est très proche de $-1$.
	
	    On peut donc dire que l'ajustement est très raisonnable.

    **3.** Question 3  
    Tracer cette droite sur le graphique et placer le point moyen de ce nuage.

    ??? success "Solution"

        La droite d'ajustement a été tracée en utilisant le point moyen et 
        $ \left\{\begin{matrix}
        x=28 \Rightarrow y=286,16 \\ 
        x=52 \Rightarrow y = 81,44 
        \end{matrix}\right.
        $
 

    **4.** Question 4   
    En utilisant cet ajustement :

	* Quel prix maximal doit-on proposer pour que plus de 60 % des personnes interrogées soient prêtes à l'acheter ?
    * Au-delà de quel prix le taux d'acheteurs potentiels tombe-t-il sous les 10 % ?

    ??? success "Solution"

        Grâce à cet ajustement on voit que :
    
        * Le prix maximal que l'on doit proposer pour que plus de 60 % des personnes interrogées (soit 300) soient prêtes à l'acheter est d'environ 26 €.
        * Au-delà de 56 €, le taux d'acheteurs potentiels tombe sous 50 %.


   





