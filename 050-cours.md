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
3. l'association d'ontologies et contraintes aditonnelles, avec validation formelle (SHACL)
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

![PREMIS overview](media/PREMIS-overview.png)


---

![PREMIS overview](media/PREMIS-objects.png)

---

PREMIS peut être combiné à RiC-O:

| PREMIS | RiC-O |
|--------|-------|
| - | RecordSet RiC-E03 |
| Intellectual entity | Record RiC-E04 |
| Representation | Instantiation RiC-E06 |
| File | - |
| Datastream | - |


### 3. Association d'ontologies et contraitnes (SHACL)
 

* définition de l'articulation des ontologies (ex. combinaison RiC et PREMIS)
* contraintes personaliées à souhait (ex. minimum un agent-auteur avec numéro AVS valide)
* validation fermée ou ouverte à choix (permet de la souplesse... ou pas)
* permet d'étendre à volonté l'ontologie descriptive (ex. RiC+SKOS+EbuCore ou DublinCore+SKOS+RDAU)

***=> respect d'un schéma rigoureux garanti essentiel à la préservation***

---

### Extenstion de la description

Quelques ontologies descriptives à considérer:

* [DublinCore](https://www.dublincore.org) : [Element Set](https://www.dublincore.org/specifications/dublin-core/dces/) et [DCMI Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/)
* [RDA-U](http://www.rdaregistry.info/Elements/u/) : Research Data Alliance - nombreuses propriétés concernant les records et agents
* [EBU-core](https://tech.ebu.ch/publications/tech3293) : Eurovision data model - multimedia
* [IFLA-LRM](https://repository.ifla.org/handle/123456789/40) : Library Reference Model - nouvelle évolution après FRBR
* [CIDOC-CRM](https://www.cidoc-crm.org/) : Musées

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

# Intégration

---

[Animation d'intégration](./media/integration.pptx)

---

# Discussion

---

La combinaision de ces standards et outils permet:

1. Généraliser la description / catalogage
2. Préservation à long terme
3. Une excellente interopérabilité (cf. cours suivant)


---

### 1. Généralisation de la description

* Richesse des ontologies "métier": [LOD cloud](https://lod-cloud.net/)
* Interconnexions (owl:sameAs) entre les ontologies
* Les contraites d'accès pour les usagers tombent (ISAD(G): accès selon la structure arborescente des fonds imposée)


---

*** Focus sur la structure***

P.ex. RiC, et les technologies du Web sémantique en général, offre un accès multi-dimentionnel (pas seuleuement selon un arbre):

* Les "records sets" ne sont plus limités a une structure aborscente bi-dimentionnelle.
* D'abord, l'arbre peut changer dans le temps => structure tri-dimentionnelle.
* Plusieurs regroupements intellectuels peuvent être faits et combinés (rico:proxy).
* L'accès par d'autre types d'objets (agents, sujets, lieux, fonctions, etc.) est facilité.

---

# 2. Préservation

---

* Les containers LDP permettent de regrouper le RDF relatif aux objets à présserver (dossiers, documents ou autre).
* OCFL permet de gérer les diverese verions des objets à préserver dans les AIP de façon faible et portable (voir de plus les 5 objectifs).
* Le concept d'*unité archivistique* (*archival unit*) permet de regrouper les objets qui vont ensemble (p. ex. un dossier et ses documents).
* Le RDF, basé sur le concept sujet-objet-prédica, est une structure universelle et de ce fait épargnée par l'obsolescence technologique.  

---

# 3. Interopérabilité

---

Est très élevée, par nature même de la technologie choisie le but premier du Web sémantique.

Ceci sera développé dans la prochaine et dernière session de ce cours.

---

# Questions et réponses

---

