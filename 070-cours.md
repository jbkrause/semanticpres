---
author: "Jan Krause-Bilvin"
title: "HEG-796-22-070"
subtitle: "Valorisation"
date: 2022-06-08
lang: fr-CH
presention: "pandoc -t revealjs -s -o 070-cours.html 070-cours.md -V revealjs-url=reveal.js -V theme=league --katex; pandoc -t html5 -o 070-cours.pdf 070-cours.md"
encoding: utf-8

---

# Mise en oeuvre

---

Conetenu de cette session:

1. Valorisation et Indexation  
2. Plateforme LDP: documentation de Fedora Commons
3. Triple store: Blazegraph 

---

### Avant de débuter

-> Évaluation de ce cours en ligne sur le portail AGE. 

---

# 1. Valorastion et indexation

---

### Rappel 

[Animation d'intégration](./media/integration.pptx)

---

### Besoin de "scalability"

En français, on pourrait dire d'"évolutivié". Il y a une dimention d'échelle.

En pratique, considérons les concepts suivants:

* Messaging
* Conteneurs 
* Fault-tolerence

---

### Messaging

Dans les application modernes, on utilise souvent le concept de ***messaging***.

Par exemple, la technologie [Apache Caml](https://camel.apache.org/) dont [Apache Kafka](https://www.youtube.com/watch?v=PzPXRmVHMxI).

---

### Conteneurs

Dans les application modernes, on utilise souvent le concept de ***conteneurs***, une façon de déployer des applications encore plus efficiente que la virtualisation.

Par exemple, la technologie [docker](https://www.youtube.com/watch?v=8cH0ilGlQdE), voir aussi cette [video](https://www.youtube.com/watch?v=0HjPvbGSdoo).

De plus, des systèmes d'orchestration permettent d'orchester les containers, p.ex. [kubernetes](https://www.youtube.com/watch?v=PziYflu8cB8).

---

### Fault tolerence

Éviter la corruption: le problème des Généraus Bizantins.

![](media/Byzantine-generals.png)

Il est démontré que pour tolérer f fautes, 3f+1 noeuds sont nécessaires. Cf. travaux de Lesslie Lamport fin des années 1970.

---

Vidéos explicatives:

* [introduction](https://www.youtube.com/watch?v=LoGx_ldRBU0)
* [introduction visuelle](https://www.youtube.com/watch?v=A-mNgqJETQg)
* [lien avec la blockchain](https://www.youtube.com/watch?v=0lkhrobRTdo)
* [proof of work](https://www.youtube.com/watch?v=3EUAcxhuoU4&t=69s)
* [proof of work vs. proof of stake](https://www.youtube.com/watch?v=M3EFi_POhps)

---

### Résumé

* Messaging : optimiser le transfert de données entre les composants du système d'archivage
* Conteneurs : optimiser la charge des dans les datacenter et la protabilité (dépendances)
* Fault-tolerence : garantir la cohérence des données (prévention priratage et intégrité des données)

Fedora Commons est construit sut la base de ces techonologies.

---

# 2. Plateforme LDP: documentation de Fedora Commons

---

[Lyrasis - Fedora Commons - Documentation](https://wiki.lyrasis.org/display/FEDORA6x/Fedora+6.x+Documentation)

* Architecture
* [Installation](https://wiki.lyrasis.org/display/FEDORA6x/Quick+Start) (one click , docker)
* [Configuration](https://wiki.lyrasis.org/display/FEDORA6x/Configuration)(paramètres)
  * [configuration docker](https://github.com/fcrepo-exts/fcrepo-docker/blob/main/README.md) (users, praramètres:fcrepo.properties)
  * [liste des paramètres](https://wiki.lyrasis.org/display/FEDORA6x/Properties)
    * exemples: fcrepo.external.content.allowed, fcrepo.autoversioning.enabled, fcrepo.metrics.enable

---

* Mesasging
* External Search
* Metrics
* Auto-versionning
* Namespaces

---

3. Triple store: Blazegraph

---


  

  


