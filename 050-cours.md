---
author: "Jan Krause-Bilvin"
title: "HEG-796-22-050"
subtitle: "Intégration et discussion"
date: 2022-04-11
lang: fr-CH
presention: "pandoc -t revealjs -s -o 050-cours.html 050-cours.md -V revealjs-url=reveal.js -V theme=league --katex; pandoc -t html5 -o 050-cours.pdf 050-cours.md"
encoding: utf-8
---

# Récapituation et intégration

---

### Ontologies (OWL)

Exemples abordés dans ce cours:

  * structurelles (LDP - périmètre des objets)
  * descriptives (RiC)
  * préservation (PREMIS)
 
***=> un langage universel couvrant également les besoins en matière de préservation***
 
---

### Exigences (SHACL)
 

* contraintes personaliées à souhait (ex. minimum un agent-auteur avec numéro AVS valide)
* définition de l'articulation des ontologies
* validation fermée ou ouverte à choix (permet de la souplesse... ou pas)

***=> respect rigoureux des besoins spécifiques des institutions ou domaines***

---


### Interfaces (API)

* normalisation des plateformes (LDP: containers + ReST)
* versions (RFC 7089, Memento)
* cohabitation naturelle avec SPARQL endpoints

***=>Exellente interopérabilité pour diffusion (silos abbatus)***

---

### Préservation (OAIS)

OCFL a cinq objectifs principaux:
* Complétude (disater recovery)
* Parsabilité (humains et machines)
* Robustess (erreur, corruption, migrtions)
* Versionning (hisorique des objets)
* Diversité de stockage (multi-infrastructure et migrations)

---

# Discussion

---

La combinaision des technologies et permettent ensemble

* Généralisation de la description / catalogage
* Interopérabilité
* Préservation à long terme

---

### Généralisation de la description

* Richesse des ontologies: [LOD cloud](https://lod-cloud.net/)
* Interconnexions entre les ontologies (ex: archives et musées)
* Les contraites d'accès pour les usagers tombent (ISAD(G): accès selon la structure arborescente des fonds imposée)


---

***Focus sur la structure***

P.ex. RiC offre un accès multi-dimentionnel (pas seuleuement selon un arbre):

* Les "records sets" ne sont plus limités a une structure aborscente bi-dimentionnelle.
* D'abord, l'arbre peut changer dans le temps => structure tri-dimentionnelle.
* Plusieurs regroupements intellectuels peuvent être faits et combinés.
* L'accès par d'autre types d'objets (agents, sujets, fonctions, etc.) est facilité.

---

# Préservation

---

* Les containers LDP permettent de regrouper le RDF relatif aux objets à présserver (dossiers, documents ou autre).
* OCFL permet de gérer les diverese verions des objets à préserver dans les AIP de façon faible et portable (voir de plus les 5 objectifs).
* Le concept d'*unité archivistique* (*archival unit*) permet de regrouper les objets qui vont ensemble (p. ex. un dossier et ses documents).
* Le RDF, basé sur le concept sujet-objet-prédica, est une structure universelle et de ce fait épargnée par l'obsolescence technologique.  

---

# Questions et réponses

---

