---
author: "Jan Krause-Bilvin"
title: "HEG-796-22-040"
subtitle: "Valorisation"
date: 2022-06-01
lang: fr-CH
presention: "pandoc -t revealjs -s -o 050-cours.html 050-cours.md -V revealjs-url=reveal.js -V theme=league --katex; pandoc -t html5 -o 050-cours.pdf 050-cours.md"
encoding: utf-8
---

# Valoraisation

---

On peut lire dans le premier paragraphe de la norme [OAIS](https://public.ccsds.org/pubs/650x0m2.pdf):

> An OAIS is an Archive, consisting of an or ganization, 
> which may be part of a larger organization, of people 
> and systems that has accepted the responsibility to preserve
> information and ***make it available for a Designated Community***. 

=> Pas de préservation sans diffusion !

---

### Rappel - Schéma OAIS :

![OAIS schema](media/OAIS-schema-general.png)

---

### Rappel - Intégration

[Animation d'intégration](./media/integration.pptx)

---

### En Suisse

* Memoriav: 
  * [http://memobase.ch](http://memobase.ch)
  * [http://api.memobase.ch](http://api.memobase.ch)
* Archives PTT (Poste Télégrammes Téléphones)
  * https://data.ptt-archiv.ch/archive/record/202776
* Canton de Bâle-Ville
  * [SPARQL](https://ld.staatsarchiv.bs.ch/sparql/)  
* SWITCH
  * [Connectome](https://www.switch.ch/connectome/)
* Semantic AIS: Docuteam + zazuko
  
---

Démo https://ld.staatsarchiv.bs.ch/sparql/ 

```
PREFIX rico: <https://www.ica.org/standards/RiC/ontology#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT * WHERE {
  ?sub rico:title ?title .
  ?sub rico:isAssociatedWithDate ?date .
  ?date rico:expressedDate ?eDate .
  FILTER regex(?title, ".*[Pp]artei.*", "i").
  FILTER regex(?eDate, ".*1[45]\\d\\d.*", "i").
} 
LIMIT 100
```

---


### En France

* Prototype PIAAF (France)
  * https://piaaf.demo.logilab.fr/sparql
  * https://piaaf.demo.logilab.fr/editorial/help
* Archives Nationales: projet ALEGORIA
  * https://www.alegoria-project.fr/en/Metadata
  * http://data.alegoria-project.fr/page/anf%2Flapie%2Frecord%2F058220-c-70wu0l12w-14l18b4znre8s
  * http://data.alegoria-project.fr/sparql
  
  
[Autres exemples](https://ica-egad.github.io/RiC-O/projects-and-tools.html).

---

Fonds iconographique décrivant le territoire français d'entre deux guerres.

Démo: http://data.alegoria-project.fr/sparql

```
PREFIX rico: <https://www.ica.org/standards/RiC/ontology#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT * WHERE {
  ?sub rico:title ?title .
  FILTER regex(?title, ".*L[ée]man.*", "i").
} 
LIMIT 100
```

---


### Outils

* EAD et EAC [RiC-O converter](https://github.com/ArchivesNationalesFR/rico-converter)
* [Memobase, GitLab](https://gitlab.switch.ch/memoriav/memobase-2020)
* [aLOD, GitHub](https://github.com/zazuko/bar.alod.ch) 
* [Scope RDF RML Pipeline, GitHub](https://github.com/Staatsarchiv-Basel-Stadt/RDF-Pipeline), et [scope2RDF](https://github.com/Staatsarchiv-Basel-Stadt/StABS-scope2RDF)
* [RDF Mapping Language](https://rml.io/specs/rml/)
* [Large Triple Stores](https://www.w3.org/wiki/LargeTripleStores)