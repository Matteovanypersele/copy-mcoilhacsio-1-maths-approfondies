---
author: Mireille Coilhac
title: Prérequis - fonctions
tags:
    - fonctions
---

## Généralités sur les fonctions

[Généralités sur les fonctions - Prérequis](a_telecharger/generalites_fonctions.pdf){ .md-button target="_blank" rel="noopener" }

[Exercices : Généralités sur les fonctions](a_telecharger/generalites_fcts_sujet.pdf){ .md-button target="_blank" rel="noopener" }

[Correction des exercices : Généralités sur les fonctions](a_telecharger/generalites_fonctions_correction.pdf){ .md-button target="_blank" rel="noopener" }



## Prérequis sur la dérivation

[Skieur géogébra](https://www.geogebra.org/m/wemqzb3y){ .md-button target="_blank" rel="noopener" }

[Dérivation - Prérequis](a_telecharger/Derivation.pdf){ .md-button target="_blank" rel="noopener" }

## Mémorisation des formules de dérivation

??? question "$f(x) = k$"

    $f$ est définie et dérivable sur $\mathbb{R}$

    Soit $k$ un réel donné. $f(x) = k$  
    $f'(x) = ?$

    ??? success "Solution"

        $f'(x) = 0$


??? question "$f(x) = x^2$"

    $f$ est définie et dérivable sur $\mathbb{R}$

    $f(x) = x^2$  
    $f'(x) = ?$

    ??? success "Solution"

        $f'(x) = 2x$

??? question "$f(x) = x^3$"

    $f$ est définie et dérivable sur $\mathbb{R}$

    $f(x) = x^3$  
    $f'(x) = ?$

    ??? success "Solution"

        $f'(x) = 3x^2$

??? question "$f(x) = x^n$"

    $n \in $\mathbb{N}$. $f$ est définie et dérivable sur $\mathbb{R}$

    $f(x) = x^n$  
    $f'(x) = ?$

    ??? success "Solution"

        $f'(x) = nx^{n-1}$

??? question "$f(x) = \dfrac{1}{x}$"

    On se place sur $]-\infty, 0[$ ou sur $]0, +\infty[$

    $f(x) = \dfrac{1}{x}$  
    $f'(x) = ?$

    ??? success "Solution"

        $f'(x) = -\frac{1}{x^2}$

??? question "$f(x) = \dfrac{1}{x^2}$"

    On se place sur $]-\infty, 0[$ ou sur $]0, +\infty[$

    $f(x) = \dfrac{1}{x^2}$  
    $f'(x) = ?$

    ??? success "Solution"

        $f'(x) = - \dfrac{2}{x^3}$

??? question "$f(x) = \dfrac{1}{x^n}$"

    $n \in $\mathbb{N}$. On se place sur $]-\infty, 0[$ ou sur $]0, +\infty[$

    $f(x) = \dfrac{1}{x^n}$  
    $f'(x) = ?$

    ??? success "Solution"

        $f'(x) = - \dfrac{n}{x^{n+1}}$

??? question "$f(x) = \sqrt{x}$"

    $f$ est définie sur $[0, +\infty[$ et dérivable sur $]0, +\infty[$

    $f(x) = \sqrt{x}$  
    $f'(x) = ?$

    ??? success "Solution"

        $f'(x) = \dfrac{1}{2\sqrt{x}}$

??? question "$u+v$"

    On se place sur $\mathcal{D}$ l'ensemble sur lequel $u$ et $v$ sont dérivables.

    $(u+v)'=?$

    ??? success "Solution"

        $(u+v)'=u' + v'$

??? question "$ku$"

    Soit $k$ un réel donné. On se place sur $\mathcal{D}$ l'ensemble sur lequel $u$ est dérivable.

    $(ku)' = ?$

    ??? success "Solution"

        $(ku)' = ku'$

??? question "$u v$"

    On se place sur $\mathcal{D}$ l'ensemble sur lequel $u$ et $v$ sont dérivables.

    $(uv)'=?$

    ??? success "Solution"

        $(uv)'=uv' + u'v$



??? question "$\dfrac{u}{v}$"

    On se place sur $\mathcal{D}$ l'ensemble sur lequel $u$ et $v$ sont dérivables et ne s'annulent pas.

    $\left( \dfrac{u}{v} \right)'=?$

    ??? success "Solution"

        $\left( \dfrac{u}{v} \right)'= \dfrac{u'v - uv'}{v^2}$



??? question "$u^n$"

    Soit $n$ un entier naturel. On se place sur $\mathcal{D}$ l'ensemble sur lequel $u$ est dérivable.

    $\left( u^n \right)'=?$

    ??? success "Solution"

        $\left( u^n \right)'=n u' u^{n-1}$

??? question "$\dfrac{1}{u}$"

    On se place sur un ensemble sur lequel $u$ est définie et dérivable et ne s'annule jamais.

    $f(x) = \dfrac{1}{u}$  
    $f'(x) = ?$

    ??? success "Solution"

        $f'(x) -\dfrac{u'}{u^2}$

??? question "$\sqrt{u}$"

    On se place sur $\mathcal{D}$ l'ensemble sur lequel $u$ est dérivable et strictement positif.

    $f(x) = \left( \sqrt{u}\right)$   
    $f'(x) = ?$

    ??? success "Solution"

        $f'(x) = \dfrac{u'}{2\sqrt{u}}$



??? question "$\dfrac{1}{u^n}$"

    Soit $n$ un entier naturel. On se place sur $\mathcal{D}$ l'ensemble sur lequel $u$ est dérivable et non nul.

    $f(x) = \dfrac{1}{u^n}$  
    $f'(x) = ?$

    ??? success "Solution"

        $f'(x) = -\dfrac{n u'}{u^{n+1}}$

## QCM

{{ multi_qcm('qcm_derivation.json') }}

## Exercices de dérivation

[Exercices : formules de dérivation](https://coopmaths.fr/alea/?uuid=ec088&id=1AN14-3&n=5&d=10&s=6&s2=true&s3=false&alea=wu0A&cd=1&uuid=a83c0&id=1AN14-4&n=6&d=10&s=5&alea=UCY4&cd=1&uuid=1a60f&id=1AN14-5&n=5&d=10&s=6&alea=BUiw&cd=1&uuid=b32f2&id=1AN14-6&alea=naqO&uuid=3391d&id=1AN14-7&alea=wckV&v=eleve&es=0111001&title=){ .md-button target="_blank" rel="noopener" }

[Exercices : Dérivation : exercices de base](a_telecharger/Derivation_exos_revision_rectif.pdf){ .md-button target="_blank" rel="noopener" }


[Correction : Dérivation : exercices de base](a_telecharger/derivation_exos_revision_corr.pdf){ .md-button target="_blank" rel="noopener" }

## Etude d'une fonction polynôme du troisième degré

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/qrj3JzAriw8?si=JpahMOcHJnmKIZ_X" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


[Etude de fonctions polynômes du 3ème degré](https://coopmaths.fr/alea/?uuid=e1890&id=1AN20-4&n=5&d=10&s=4&cd=1&v=eleve&es=0211001&title=){ .md-button target="_blank" rel="noopener" }


## Etude d'une fonction polynôme de degré 4

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/6IVxQ6piC1c?si=LbGanWHdStc7yQEr" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


## Cours complet sur les études de fonctions

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/2Owr18MregQ?si=Oyrtkeb2WUVYZAqW" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Calculatrices graphiques et fonctions

[Calculatrices](https://mcoilhac.forge.apps.education.fr/prerequis-maths-premiere/calculatrice/calculatrices/){ .md-button target="_blank" rel="noopener" }

## Vérifier avec du calcul formel

Vous pouvez vous entraîner et vérifier vos réponses ici en utilisant la syntaxe `diff(f(x), x)` comme par exemple :  `diff(x**3, x)`

[Calcul formel](https://mcoilhac.forge.apps.education.fr/tester-code-calcul-formel-graphique-animation-avec-python/sympy_formel/sympy_formel/){ .md-button target="_blank" rel="noopener" }

## Crédits

D'après des documents de Cédric Pierquet.