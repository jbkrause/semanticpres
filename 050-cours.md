---
author: "Jan Krause-Bilvin"
title: "HEG-796-22-050"
subtitle: "Intégration et discussion"
date: 2022-05-17
lang: fr-CH
presention: "pandoc -t revealjs -s -o 050-cours.html 050-cours.md -V revealjs-url=reveal.js -V theme=league --katex; pandoc -t html5 -o 050-cours.pdf 050-cours.md"
encoding: utf-8
---

# Récapituation et intégration


---

### Thématiques couvertes dans ce cours

Modélisation de: 

1. la description (Ontologie RiC)
2. la préservation (Ontologie PREMIS)
3. l'association d'ontologies et contraintes aditonnelles, avec validation (SHACL)
4. l'empaquetage de ressources RDF et binaires et de leur versionnage (contaners LDP, Fedora Commons)
5. la préservation des containers LDP versionnés dans des AIP selon la norme OAIS (OCFL,Fedora Commons)

---

### 1. Description Ontologie RiC

* Record ressources : collections, fonds, séries, dossiers, documents
* Instanciations : item ou article à proporent dit (fichiers, objets physiques)
* Événements : création, clôtrue, etc.
* Lieux : géographie
* Dates : ponctuelles, liste ou plages
* Agents : groupes, presonnes morales ou physiques, agents logiciels

*** => description complète et normalisée (Web sémantique va au delà de notre domaine)***
 
---

![RiC overview](media/RiC-CM-overview.jpg)

---

### 2. Métadonnées de préservation (PREMIS)

---

### 3. Association d'ontologies et contraitnes (SHACL)
 

* définition de l'articulation des ontologies (ex. combinaison RiC et PREMIS)
* contraintes personaliées à souhait (ex. minimum un agent-auteur avec numéro AVS valide)
* validation fermée ou ouverte à choix (permet de la souplesse... ou pas)

***=> respect d'un schéma rigoureux garanti essentiel à la préservation***

---


### 4. Empaquetage des ressources RDF et binaires (LDP)

* Containers LDP permettent de conditionner les ressources de façon à ce qu'elles coresspondent aux objets à archiver (dossiers, documents, etc.).
* Gestion des versions des objets (RFC 7089, Memento)
* Normalisation de la manipulation des containers (création, modification, etc.)

***=> Adéquation avec le objets métier à archiver et interopérabilité***

---

### 5. Préservation (OAIS, OCFL)

Chaque objet OCFL peut archiver un ou plusieur container LDP. OCFL a cinq objectifs principaux:
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

