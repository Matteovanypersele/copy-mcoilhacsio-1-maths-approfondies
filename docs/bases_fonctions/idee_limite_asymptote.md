---
author: Mireille Coilhac
title: Initiation aux limites et asymptotes
tags:
    - fonctions
---

## I. Limites infinies

???+ question "Un premier exemple"

    Observons la représentation graphique de la fonction $f$.

    ![moins_inf_en_plus_inf.PNG](images/moins_inf_en_plus_inf.PNG){ width=10% }

    Lorsque $x$ devient "très très grand", c'est-à-dire lorsque $x$ se "rapproche" de $+ \infty$, on voit que $f(x)$ se "rapproche" de $- \infty$.   
    On dit que lorsque $x$ **tend** vers $+ \infty$, alors $f(x)$  **tend** vers $- \infty$.  

    On note : 

    !!! info "Notattion"

        On note : 
        
        $$
        \lim_{x\to +\infty} f(x) = -\infty
        $$

        On lit : "la limite lorsque $x$ tend vers $+\infty$ de $f(x)$ est égale à $-\infty$"

???+ question "Un deuxième exemple"

    Observons la représentation graphique de la fonction $f$.

    ![plus_inf_en_moins_inf.PNG](images/plus_inf_en_moins_inf.PNG){ width=10% }

    par analogie, donner la limite de $f$ que l'on peut observer

    ??? success "Solution"

        $$
        \lim_{x\to -\infty} f(x) = +\infty
        $$

        On lit : "la limite lorsque $x$ tend vers $-\infty$ de $f(x)$ est égale à $+\infty$"


???+ question "Un troisième exemple"

    Observons la représentation graphique de la fonction $f$.

    ![inf_en_3_moins.PNG](images/inf_en_3_moins.PNG){ width=15% }

    Lorsque $x$ devient de plus en plus proche de 3, en restant inférieur à 3, on voit que $f(x)$ se "rapproche" de $+ \infty$.   
    On dit que lorsque $x$ **tend** vers 3 en étant inférieur 3, alors $f(x)$  **tend** vers $+ \infty$.  

    !!! info "Notation"

        On note : 
            
        $$
        \lim_{\substack{x\to 3 \\ x<3}} f(x) = +\infty
        $$

        On lit : "la limite lorsque $x$ tend vers 3 avec $x$ inférieur 3, de $f(x)$ est égale à $+\infty$"

    !!! info "Asymptote"

        On observe que la courbe représentative de la fontion $f$ notée $C_f$ "s'approche" de plus en plus de la droite d'équation $x=3$ lorsque $x$ tend vers 3.

        **On dit que la droite d'équation $x=3$ est une asymptote verticale à la courbe $C_f$**


???+ question "Un quatrième exemple"

    Observons la représentation graphique de la fonction $f$.

    ![inf_en_3_plus.PNG](images/inf_en_3_plus.PNG){ width=15% }

    Lorsque $x$ devient de plus en plus proche de 3, en restant supérieur à 3, on voit que $f(x)$ se "rapproche" de $+ \infty$.   
    On dit que lorsque $x$ **tend** vers 3 en étant supérieur à 3, alors $f(x)$  **tend** vers $+ \infty$.  

    !!! info "Notation"

        On note : 
            
        $$
        \lim_{\substack{x\to 3 \\ x>3}} f(x) = +\infty
        $$

        On lit : "la limite lorsque $x$ tend vers 3 avec $x$ supérieur à 3, de $f(x)$ est égale à $+\infty$"

    !!! info "Asymptote"

        On observe que la courbe représentative de la fontion $f$ notée $C_f$ "s'approche" de plus en plus de la droite d'équation $x=3$ lorsque $x$ tend vers 3.

        **On dit que la droite d'équation $x=3$ est une asymptote verticale à la courbe $C_f$**


