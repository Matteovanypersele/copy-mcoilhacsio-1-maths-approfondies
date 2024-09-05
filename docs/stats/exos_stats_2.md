---
author: Mireille Coilhac
title: Exercices - statistiques à deux variables
tags:
    - statistiques
---

## Exercice 1

???+ question "Exercice 1"

    Lors d'une enquête réalisée auprès de 500 personnes, on a estimé le nombre de personnes prêtes à acheter un nouveau produit en fonction du prix de ce produit :

    * $x_i$ est le prix proposé en euros
    * $y_i$ est le ombre d'acheteurs potentiels
    
    Prix proposé en euros ($x_i$) | 52 | 47 | 44 | $38,5$ | $35,5$ | 32 | 31 | 28 |
    |:---|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
	Nombre d'acheteurs potentiels ($y_i$) | 80 | 125 | 145 | 200 | 225 | 250 | 265 | 280|

    $$\begin{array}{|l|c|c|c|c|c|c|c|c|}
    \hline
	x_i & 52 & 47 & 44 & 38,5 & 35,5 & 32 & 31 & 28 \\
    \hline
	y_i &80& 125& 145& 200& 225& 250& 265& 280\\
    \hline
    \end{array}$$


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
        $\left\{\begin{matrix}
        x=28 \Rightarrow y=286,16 \\ 
        x=52 \Rightarrow y = 81,44 
        \end{matrix}\right.$


    **4.** Question 4   
    En utilisant cet ajustement :

	* Quel prix maximal doit-on proposer pour que plus de 60 % des personnes interrogées soient prêtes à l'acheter ?
    * Au-delà de quel prix le taux d'acheteurs potentiels tombe-t-il sous les 10 % ?

    ??? success "Solution"

        Grâce à cet ajustement on voit que :
    
        * Le prix maximal que l'on doit proposer pour que plus de 60 % des personnes interrogées (soit 300) soient prêtes à l'acheter est d'environ 26 €.
        * Au-delà de 56 €, le taux d'acheteurs potentiels tombe sous 50 %.

## Exercice 2

???+ question "Exercice 2"

    Le tableau ci-dessous donne les quantités de marchandises transportées dans le monde par voie maritime entre 2000 et 2017, exprimées en millions de tonnes.  
    
    * $x_i$ est le rang de l'année
    * $y_i$ est la quantité de marchandises en millions de tonnes

    $$\begin{array}{|l|c|c|c|c|c|c|c|c|c|c|}
    \hline
	\text{Année} & 2000& 2005& 2010& 2011& 2012& 2013 &2014& 2015& 2016 &2017\\
    \hline
	x_i &0& 5& 10& 11& 12& 13& 14& 15& 16& 17\\
    \hline
	y_i & 5984 & 7109 & 8409 & 8784 & 9197 & 9548 & 9842 & 10024 & 10289 & 10702\\
    \hline
    \end{array}$$



    Le nuage de points de coordonnées $(x_i;y_i)$ est donné ci-dessous :

    ![nuage_exo_2_doubles](images/nuage_exo_2_doubles.png){ width=50% }

    **1.** Question 1  
    Expliquer pourquoi ce nuage de points permet d'envisager un ajustement affine.

    ??? success "Solution"

        Le nuage de points a une forme allongée, donc un ajustement affine est envisageable.

    **2.** Question 2  
    Déterminer à l'aide de la calculatrice l'équation réduite de la droite d'ajustement de $y$ en $x$ obtenue par la méthode des moindres carrés. On arrondira les coefficients au dixième.

    ??? success "Solution"

        La calculatrice donne $y = 281,0x + 5813,4$ avec les coefficients arrondis au dixième.

    **3.** Question 3  
    On décide de modéliser la quantité de marchandises $y$ en fonction du rang de l'année $x$ par l'expression $y = 280x + 5800$.

    Tracer la droite $D$ d'équation $y = 280x + 5800$ dans un repère identique à celui donné précédemment.

    ??? success "Solution"

        ![nuage_exo_2_doubles](images/graphe_exo_2_doubles.png){ width=50% }

    **4.** Question 4  
    Estimer, selon le modèle de la question 3, la quantité de marchandises transportées par voie maritime en 2025, en expliquant la démarche suivie.

    ??? success "Solution"

        Dans cette question, il s'agit de faire une prévision pour $x=25$ :
	
	    * pour $x = 25$ on lit pour $y$ environ 12800;
	    * avec $x = 25$, on obtient $y = 280\times 25 + 5800 = 7000 + 5800 = 12800$.
	
	    Ainsi on on obtient une estimation de 12800 millions de tonnes.

## Exercice 3

À venir ...

<!-- 

???+ question "Exercice 3"

    Dans le tableau suivant figure une partie des résultats d'une enquête réalisée par une entreprise pour 
    déterminer le nombre d'acheteurs potentiels de ce nouveau produit en fonction de son prix de vente :

    * $x_i$ est le prix de vente en euros
    * $y_i$ est le nombre d'acheteurs potentiels

    $$\begin{array}{|l|c|c|c|c|c|c|}
    \hline
	x_i  & 200 & 250 & 300 & 350  & 450 & 500 \\
    \hline
	y_i & 632 & 475 & 305 & 275 & 266 & 234 \\
    \hline
	\end{array}$$

    **1.** Question 1
    Est-il judicieux de réaliser un ajustement affine pour ce nuage ?

    ??? success "Solution"

        A venir

    **2.** Question 2   
    on effectue le changement de variable $z_i = \ln( y_i)$.

    Recopier et compléter le tableau de valeurs suivant (les valeurs demandées seront arrondies au millième) :

    $$\begin{array}{|l|c|c|c|c|c|c|}
    \hline
	x_i  & 200 & 250 & 300 & 350  & 450 & 500 \\
    \hline
	z_i = \ln(y_i) & 6,449 & 6,163 &  &  &  &  \\
    \hline
	\end{array}$$

    ??? success "Solution"

        $$\begin{array}{|l|c|c|c|c|c|c|}
        \hline
			x_i  & 200 & 250 & 300 & 350  & 450 & 500 \\
            \hline
			z_i = \ln(y_i) & 6,449 & 6,163 & 5,720 & 5,617 & 5,583 & 5,455  \\
            \hline
		\end{array}$$


    **3.** Question 3

    Donner une valeur approchée à $10^{-2}$ près du coefficient de corrélation linéaire de la série statistique $(x_i;z_i)$.
	
	Le résultat obtenu permet d'envisager un ajustement affine ?

    ??? success "Solution"

        La calculatrice nous donne $r \approx -0,90$ proche de $-1$.
	
	    Donc le résultat obtenu permet d'envisager un ajustement affine.


    **4.** Question 4

    Donner, par la méthode des moindres carrés, une équation de la droite de régression de $z$ en $x$, sous la forme $z = ax+b$ 

    $a$ sera donné à $10^{-4}$ près par excès et $b$ à $10^{-2}$ près par excès.

    ??? success "Solution"

        La méthode des moindres carrés nous donne $a \approx -0,003$ et $b \approx 6,86$.

        On en déduit: $z=-0,003x+8,86$ 

    **5.** Question 5  

    En déduire une estimation du nombre d'acheteurs potentiels $y_i$ en fonction de $x_i$ sous la forme $y = k \text{e}^{-\lambda x}$ où $k$ et $\lambda$ sont des constantes ($k$ sera arrondi à l'entier le plus proche).

    ??? success "Solution"

        $z=-0,003x+8,86$
        
        donc $\text{ln}(y) = -0,003x+8,86$
        
        donc $y = \text{e}^{-0,003x+8,86} = \text{e}^{-0,003x}\times\underbrace{\text{e}^{8,86}}_{953} \approx 953\,\text{e}^{-0,003x}$.

        

    **6.** Question 6

    Utiliser cette estimation pour déterminer le nombre d'acheteurs potentiels si le prix de vente est fixé à 400 €.

    ??? success "Solution"

        Pour $x=400$, on a $y=953\times\text{e}^{-0,003\times400} \approx 287$, soit 287 acheteurs potentiels si le prix de vente est fixé à 400 €.
    


-->

















   





