---
author: Mireille Coilhac
title: Les suites
tags:
    - suites
---

## Introduction

[Cours sur les suites vu en SIO 1](https://mcoilhac.forge.apps.education.fr/sio-1-maths-approfondies/suites/intro_suites/){ .md-button target="_blank" rel="noopener" }

## Premiers exercices

???+ question "Exercice 1 : le pétrole"

     Une estimation grossière des réserves totales de pétrole et de gaz sous le plateau continental  norvégien au début de l'année 1999 était de 13 milliards de tonnes (ou équivalent pétrole). On a extrait cette année-là environ 250 millions de tonnes.

    **1.** Dans l'hypothèse où l'extraction va se maintenir à ce niveau constant, quand les réserves seront-elles épuisées ?

    ??? success "Solution"

        Si chaque année l'extraction est constante, les réserves (en millions de tonnes) forment une suite arithmétique de raison $-\np{250}$. On peut poser $u_0 = 13000$ pour les réserves en 1999. Puis $u_1$ en 2000, etc.

        Pour tout $n$, $u_n = u_0 -250n = 13000-250n$.

        Les réserves seront épuisées quand $u_n$ sera nul : 
        
        donc pour $13000-250n=0$
        
        donc pour $n = \dfrac{13000}{250}=52$ : en 2051.

    **2.** Si l'extraction est réduite de $2\%$ chaque année à partir de début 1999, combien de temps vont durer les réserves ?

    ??? success "Solution"


        en 1999, on extrait 250 (millions de tonnes) ;  
        en 2000 ($1999+1$), on extrait $250\times 0,98$  
        en $1999+n$, on extrait $250\times 0,98^n$  
        On pourrait extraire jusqu'à ce que :  

        $$250 + 250\times 0,98 + \dots +  250\times 0,98^n \geqslant 13000$$

        C'est la somme de $n+1$ termes d'une suite géométrique de raison $0,98$ :  

        $$250 \times \frac{1-0,98^{n+1}}{1-0,98} \geqslant 13000$$

        On peut tâtonner avec la calculatrice jusqu'à dépasser 13000. Mais on n'y arrive pas.

        En fait l'inégalité s'écrit :
        
        $$12500 \left(1-0,98^{n+1}\right) \geqslant 13000$$

        Le côté gauche est inférieur à 12500 pour tout $n$ : on ne dépassera jamais 13000. 

    



## Exercices de synthèse

[Exercices corrigés sur les suites géométriques](a_telecharger/exos_suites_geom.pdf.pdf){ .md-button target="_blank" rel="noopener" }

[Exercice difficile avec la fonction exponentielle](https://coopmaths.fr/alea/?uuid=bac_2022_05_sujet1_etrangers_3&v=eleve&es=0211001&title=){ .md-button target="_blank" rel="noopener" }




