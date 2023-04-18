---
author: "Jan Krause-Bilvin"
title: "HEG-796-22-EXA-8"
subtitle: "Questions d'examen"
date: 2023-04-18
lang: fr-CH
encoding: utf-8
presention: "pandoc -t revealjs -s -o EXA.html EXA.md -V revealjs-url=reveal.js -V theme=white --katex; pandoc -t html5 -o 030-tp.pdf 030-tp.md"
---

# Question 8 : OCFL - invnetaire



Considérons la représentation simplifiée d'uninventaire OCFL:

```
manifest:
  - 50a5c087f450 : "v1/content/fcr-container.nt"
  - 30a510691454 : "v1/content/documents/1/I1/file0"
  - 40152f82f455 : "v2/content/fcr-container.nt"
  - 20a5c089f45d : "v2/content/documents/1/I2/file0"

versions:
  - v1
    - state
	   - 50a5c087f450 : "fcr-container.nt"
       - 30a510691454 : "documents/1/I1/file0"  
  - v2
    - state
	   - 40152f82f455 : "fcr-container.nt"
       - 30a510691454 : "documents/1/I1/file0"  
       - 20a5c089f45d : "documents/1/I2/file0" 
```

Combien de fichers existe-il dans la version v2?

Quels fichiers ont été mis-à-jour entre la version v1 et v2?

Quels fichiers ont été ajoutés entre la version v1 et v2?

Quels fichiers ont été supprimés entre la version v1 et v2?




