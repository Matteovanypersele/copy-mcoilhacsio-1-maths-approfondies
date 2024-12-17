---
author: Mireille Coilhac
title: Logarithme népérien - Cours
tags:
    - fonctions
---

## I. Définition 1 : fonction réciproque de la fonction exponentielle

!!! info "Définition"

    La fonction logarithme népérien, notée $\text{ln}$ est  définie sur $]0;+ \infty[$

    $x>0$ et $y=\text{ln}(x) \Leftrightarrow x=\text{e}^y$ 


???+ question "Conséquences"

    **Compléter**

    $\text{e}^0=... \Leftrightarrow ...$

    $\text{e}^1=... \Leftrightarrow ...$

    $\text{e}^{-1}=... \Leftrightarrow ...$

    ??? success "Solution"

        $\text{e}^0=1 \Leftrightarrow \text{ln}(1)=0$

        $\text{e}^1=\text{e} \Leftrightarrow \text{ln}(\text{e})=1$

        $\text{e}^{-1}=\dfrac{1}{\text{e}} \Leftrightarrow \text{ln}(\dfrac{1}{\text{e}})=-1$



???+ question "Représentation graphique"

    **1.** Compléter le tableau suivant en utilisant la calculatrice :

    $$
    \begin{array}{|c|c|c|c|c|c|c|c|c|c|c|c|c|c|}
    \hline
    x & 0.1 & 0.2& 0.5& 1&2&4&6&8&10&12&14&16&18 \\
    \hline
    \text{ln}(x) &   &  & & & & & & & & & & &  \\
    \hline
    \end{array}
    $$

    ??? success "Solution"

        $$
        \begin{array}{|c|c|c|c|c|c|c|c|c|c|c|c|c|c|}
        \hline
        x & 0.1 & 0.2& 0.5& 1&2&4&6&8&10&12&14&16&18 \\
        \hline
        \text{ln}(x) & -2.3  & -1.6 & -0.7& 0& 0.7& 1.4& 1.8& 2.1&2.3 &2.5 &2.6 & 2.8&  2.9\\
        \hline
        \end{array}
        $$

    **2.** Faire la représentation graphique de la fonction $\text{ln}$

    ??? success "Solution"

        ![ex01](images/ln.png){ width=60% }


??? note "fonctions réciproques et représentations graphiques"

    Les fonctions exponentielle et logarithme népérien étant récipriques l'une de l'autre, leurs courbes 
    représentatives sont symétriques par rapport à la droite d'équation $y=x$

    ![reciproques](images/expo_ln.png){ width=40% }


## II. Propriétés algébriques

???+ question "Exercice 1"

    En utilisant la calculatrice déterminer :

    * $\text{ln}(6)$
    * $\text{ln}(2) + \text{ln}(3)$
    * $\text{ln}(\dfrac{3}{2})$
    * $\text{ln}(3) - \text{ln}(2)$
    * $\text{ln}(2^{10})$
    * $10 \times \text{ln}(2)$


???+ question "Règles ce calcul"

    On suppose que $a>0$ et $b>0$

    Compléter dans chaque cas : 

    **$\text{ln}(ab) =$**

    ??? success "Solution"

        **$\text{ln}(ab) =\text{ln}(a)+ \text{ln}(b)$**

    **$\text{ln}(\dfrac{a}{b}) =$**

    ??? success "Solution"

        **$\text{ln}(\dfrac{a}{b}) =\text{ln}(a)- \text{ln}(b)$**

    **$\text{ln}(\dfrac{1}{a}) =$**

    ??? success "Solution"

        **$\text{ln}(\dfrac{1}{a}) =-\text{ln}(a)$**

    **$\text{ln}(a^n) =$**

    ??? success "Solution"

        **$\text{ln}(a^n) =n\text{ln}(a)$**

???+ question "Exercice 2"

    <iframe src="https://euler-ressources.ac-versailles.fr/wims/wims.cgi?module=adm/raw&job=lightpopup&emod=H6/analysis/logexp1.fr&parm=cmd=new;exo=transflogexp;confparm1=1;confparm1=2;confparm1=3;confparm1=4;confparm1=5;confparm1=6;confparm1=7;confparm1=8;confparm1=9;confparm1=10;qnum=1;scoredelay=;seedrepeat=0;qcmlevel=1&option=noabout" width="100%" height="600"></iframe>












