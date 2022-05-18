---
author: "Jan Krause-Bilvin"
title: "HEG-796-22-060"
subtitle: "Valorisation"
date: 2022-05-18
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

***=> Pas de préservation sans diffusion !***

---

### Rappel - Schéma OAIS :

![OAIS schema](media/OAIS-schema-general.png)

---

### Rappel - Intégration

[Animation d'intégration](./media/integration.pptx)

---

### AAS Ensemen

Groupe de travail de l'association des archivstes suisse: [ENSEMEN](https://vsa-aas.ch/arbeitsgruppen/projektgruppe-ensemen/)

cf. les documents porduits.

---


### Memoriav

**Mission** :  Memoriav s’engage activement et durablement pour la sauvegarde, la mise en valeur et l’utilisation à grande échelle
du patrimoine audiovisuel sur tout le territoire de la Suisse. Memobase est la plateforme de Memoriav, il s'agit d'un aggrégateur national des ressources multi-media. 

* Web: [memobase.ch](http://memobase.ch)
* API: [api.memobase.ch](http://api.memobase.ch)
* Code open source: [Memobase 2020](https://gitlab.switch.ch/memoriav/memobase-2020)
* Documentation: [Modèle de données basé sur RiC-O](https://ub-basel.atlassian.net/wiki/spaces/MD/pages/331939971/Datenmodell)

  
---

### Archives PTT (Poste Télégrammes Téléphones)

Le musée de la communication est une fondation financée par La Poste et Swisscom, qui, partagent des archives communes.

La fondation a choisi RiC-O comme schéma de base pour sa salle de lecture virtuelle (prototype) qui regroupe les collections muséales (MuseumPlus), 
de bibliothèque (Swisscovery) et d'archives (ScopeArchiv)

---

![Salle de lecture virtuelle](PTT_archiv_aggregation.png)

Source: [Présentation de Nicolas Kessler, 2022](https://vsa-aas.ch/wp-content/uploads/2022/03/2022-03-25-Pr%C3%A4sentation-2-Nicolas-Kessler-VSA-Projektgruppe-ENSEMEN.pdf)

---

* Web: [data.ptt-archiv.ch](https://data.ptt-archiv.ch/archive/record/202776)
* Code open source: vairante de [www.alod.ch](https://github.com/zazuko/www.alod.ch) , [bar.alod.ch](https://github.com/zazuko/bar.alod.ch)
  
---
  
### Archives du Canton de Bâle-Ville

* [SPARQL](https://ld.staatsarchiv.bs.ch/sparql/) 
* Mise-à-jour quotidienne depuis ScopeArchiv:
  * [Pipeline - open source code](https://github.com/Staatsarchiv-Basel-Stadt/RDF-Pipeline)
  * [Mappings - open source code](https://github.com/Staatsarchiv-Basel-Stadt/StABS-scope2RDF)
  * [Stardog triple store docker - open source code](https://github.com/Staatsarchiv-Basel-Stadt/stardog-docker)
 
Le pipeline ScopeArchi peut être intérassant comme phase de transition.
 
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

***Liste des prédicats RiC-O utilisés***

```
PREFIX rico: <https://www.ica.org/standards/RiC/ontology#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT DISTINCT ?pred WHERE {
  ?sub ?pred ?obj .
  FILTER(regex(str(?pred), "RiC" ) )
} 
LIMIT 100
```

---

### Semantic AIS

En stade précoce: 

* Projet AtoM3 : [accesstomemoryfoundation.org](https://accesstomemoryfoundation.org/development/)
* Chez [docuteam](https://docuteam.ch)
  
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

***Titre et agents***

```
PREFIX rico: <https://www.ica.org/standards/RiC/ontology#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT * WHERE {
  ?record rico:title ?title .
  ?record ?rel ?agent .
  FILTER (?rel = rico:hasCreator || ?rel = rico:createdBy || ?rel = rico:hasPublisher || ?rel = rico:recordIsSourceOfAuthorshipRelation)
  ?agent  rico:hasAgentName ?agentName .
  ?agentName  rico:normalizedValue ?agentLabel .
} 
LIMIT 100
```

---

***Lieux et coordonnées***

```
PREFIX rico: <https://www.ica.org/standards/RiC/ontology#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT * WHERE {
    ?subj     rico:hasOrHadLocation ?place .
    ?place    rico:hasOrHadPhysicalLocation ?physloc .
    ?physloc rico:hasOrHadCoordinates ?coordinates .
}
LIMIT 100

```

---

***Combinaision agent et lieu***


```
PREFIX rico: <https://www.ica.org/standards/RiC/ontology#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT * WHERE {
  ?record rico:title ?title .
  OPTIONAL { ?record  rico:hasCreator ?agent . }
  OPTIONAL { ?agent   rdfs:label ?agentLabel . }
  OPTIONAL { ?record  rico:hasOrHadLocation ?place . }
  OPTIONAL { ?place   rico:hasOrHadPhysicalLocation ?physloc . }
  OPTIONAL { ?physloc rico:hasOrHadCoordinates ?coordinates . }
}
LIMIT 100

```

---

***Liste des prédicats RiC-O utlisés***

```
PREFIX rico: <https://www.ica.org/standards/RiC/ontology#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT DISTINCT ?pred WHERE {
  ?sub ?pred ?obj .
  FILTER(regex(str(?pred), "RiC" ) )
} 
LIMIT 100
```

---

### SWITCH Connectome

> Connecting open research data (ORD) to make it accessible, 
> interoperable and valuable for research, education and innovation.

[Connectome](https://www.switch.ch/connectome/)

---


### Conversion EAD et EAC en RiC


* EAD et EAC [RiC-O converter](https://github.com/ArchivesNationalesFR/rico-converter)

---

### Outils divers

* Conversion en RDF: [RDF Mapping Language](https://rml.io/specs/rml/)
* Triples stores performants: [Large Triple Stores](https://www.w3.org/wiki/LargeTripleStores)
