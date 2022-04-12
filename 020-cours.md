---
author: "Jan Krause-Bilvin"
title: "HEG-796-22-020"
subtitle: "LDP en pratique"
date: 2022-04-11
lang: fr-CH
presention: "pandoc -t revealjs -s -o 020-cours.html 020-cours.md -V revealjs-url=reveal.js -V theme=white --katex; pandoc -t html5 -o 000-intro.pdf 000-intro.md"
encoding: utf-8
---

# Thème de cette session

---


  * Plateforme LDP [Fedora Commons](https://duraspace.org/fedora/)
  * Description archivistique [Records in Context](https://www.ica.org/fr/records-in-contexts-modele-conceptuel) et l'ontologie [RiC-O](https://www.ica.org/fr/records-in-contexts-ontology)

---

# Records in Context

---


![RiC overview](media/RiC-CM-overview.jpg)


---

Quelques concepts clés de rico (centrés sur les records):

Url de l'ontologie: [https://www.ica.org/standards/RiC/RiC-O_v0-2.html](https://www.ica.org/standards/RiC/RiC-O_v0-2.html)

* Intitulé, titre: [rico:title](https://www.ica.org/standards/RiC/RiC-O_v0-2.html#title)
* Créateur: [rico:hasCreator](https://www.ica.org/standards/RiC/RiC-O_v0-2.html#hasCreator)
* Type: [rico:hasRecordSetType](https://www.ica.org/standards/RiC/RiC-O_v0-2.html#hasRecordSetType)
* Hierarchie: [rico:hasOrHadPart](https://www.ica.org/standards/RiC/RiC-O_v0-2.html#hasOrHadPart) , [rico:isOrWasPartOf](https://www.ica.org/standards/RiC/RiC-O_v0-2.html#isOrWasPartOf)
* État: [rico:hasRecordState](https://www.ica.org/standards/RiC/RiC-O_v0-2.html#hasRecordState)
* Date: [rico:hasBeginningDate](https://www.ica.org/standards/RiC/RiC-O_v0-2.html#hasBeginningDate) , [rico:hasEndDate](https://www.ica.org/standards/RiC/RiC-O_v0-2.html#hasEndDate) 


---

# Rappel du cours précédent

---

* Les ressources LDP (ldp:Ressource) peuvent être de type RDF ou non-RDF.
* Les ressources peuvent être organisées dans des containers LDP (ldp:Container).
* Les containers peuvent être emboîtés.
* Chaque container/ressource est idientifié par son URL.

---

## Correctif exercice TP

![](media/LDP-archival-fonds/010ex1-correction.png)


---

# Gesion des containers via l'interface web

---

## Créer un container (interface Web) 

![](media/FCREPO-create.png)

---

Dans la boite de dialogue "RDF Turtle", insérer:

```
<>   
<https://www.ica.org/standards/RiC/RiC-O_v0-2.html#title>   
"Le titre du record".
```

Cliquer ensuite sur le bouton "Add" comme dans la capture d'écran ci-avant.

A noter que le container est créé comme enfant du container courrant.

---

## Modifier un container (Web) 

![](media/FCREPO-update.png)

---

Dans la boite de dialogue "Update Properties", remplacer:

```
DELETE { }
INSERT { }
```

Par

```
DELETE{ <> <https://www.ica.org/standards/RiC/RiC-O_v0-2.html#title>  "Le titre du record". }
INSERT{ <> <https://www.ica.org/standards/RiC/RiC-O_v0-2.html#title>  "Le nouveau titre du record". }
```

Puis cliquer sur le bouton "Update".

Cf. capture d'écran ci-avant.

---

## Créer une ressouce binaire

![](media/FCREPO-create-binary.png)

---

Dans la section "Create New Child Ressource", choisir "Type" : "binary" dans la liste déroulante comme dans la capture d'écran précédente.

Puis cliquer sur "Parcourir" (ou "Browse") pour sélectionner le fichier à envoyer dans Fedora.

Valider en cliquant sur le bouton "Add".



---

# Gestion des containers par HTTP

---


Les verbes standard standard sont utilisés ([API rest](https://fr.wikipedia.org/wiki/Representational_state_transfer)):

<div class="fragment" data-fragment-index="1">
  * Accéder : GET
</div>
<div class="fragment" data-fragment-index="2">
  * Créer / Mettre à jour : POST / PUT
</div>
<div class="fragment" data-fragment-index="3">  
  * Supprimer : DELETE
</div>

---

### Rappel: python

Dans le contexte de la HEG, python est installé sur les postes via l'outil Anaconda.

Pour l'exécutér, ouvrir:

```
Windows > Menu démarrer > Anaconda prompt
```

Puis tapper:

```
python
```
et enter.


---

## Accéder à une ressource

```
import requests
url = 'http://localhost:8080/rest/records/acv/D000002513'
r = requests.get(url)
print('Status code:', r.status_code)
print(r.text)

```


---

## Créer un container

```
import requests
url = 'http://localhost:8080/rest/records/acv/D9999'
headers = {"Content-Type": "text/turtle"}
auth = ('fedoraAdmin', 'fedoraAdmin')
data = """ <>  <rico:title> 'Ceci est le titre'.
		   <>  <rico:scopeAndContent>   'Voilà la description'.
		   """
r = requests.put(url, auth=auth, data=data.encode('utf-8'), headers=headers)
print( 'Status:', r.status_code )
print( r.text )
```

---


## Mettre à jour un container

```
import requests
url = 'http://localhost:8080/rest/records/acv/D9999'
headers = {"Content-Type": "text/turtle"}
auth = ('fedoraAdmin', 'fedoraAdmin')
data = """ <>  <rico:title> 'Ceci est le titre mis-à-jour.'.
		   <>  <rico:scopeAndContent>   'Et la description revue'.
		   """
r = requests.put(url, auth=auth, data=data.encode('utf-8'), headers=headers)
print( 'Status:', r.status_code )
print( r.text )
```

Voir les section Versionning : "View Versions"

---



## Créer une ressource binaire

Le code suivant suppose qu'une ressouce binaire nomée "image.jpg" se trouve dans le répertoire "Images" (et que Python a été lancé depuis votre répertoire personnel racine).

```
import requests
filename = 'Pictures\\image.jpg'
mimetype = 'image/jpeg'
data = open(filename,'rb').read()
url = 'http://localhost:8080/rest/records/acv/D9999/binary'
auth = ('fedoraAdmin', 'fedoraAdmin')
headers = { "Content-Type": mimetype,
			"Link" :"<http://www.w3.org/ns/ldp#NonRDFSource>; rel=type"}
r = requests.put(url, auth=auth, data=data, headers=headers)
print( 'Status:', r.status_code )
print( r.text )
```

---

# Versionning RFC7099 (Memento)

---

* Par défaut, Fedora Commons conserve toutes les versions des ressources. 
* Il est possible de personnaliser ce fonctionnement.
* Cela perment de naviguer dans le temps (p.ex. mise à jour du plan de classement)

---
