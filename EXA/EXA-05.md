---
author: "Jan Krause-Bilvin"
title: "HEG-796-22-EXA-5"
subtitle: "Questions d'examen"
date: 2023-04-18
lang: fr-CH
encoding: utf-8
presention: "pandoc -t revealjs -s -o EXA.html EXA.md -V revealjs-url=reveal.js -V theme=white --katex; pandoc -t html5 -o 030-tp.pdf 030-tp.md"
---

# Question 5 : SHACL - dossier et date

---

Expliquer et commenter le code SHACL ci-dessous:

```
archvd:DossierShape
	a sh:NodeShape ; 
	sh:targetClass  archvd:Dossier ;

		sh:property [
			sh:path rico:isOrWasPartOf ;
			sh:nodeKind sh:IRI ;
			sh:minCount 1 ;
		] ;	
		
		sh:property [
			sh:path ldp:contains ;
			sh:nodeKind sh:IRI ;
			sh:minCount 1 ;
		] ;	
		
		sh:property [
			sh:path rico:title;
			sh:datatype xsd:string ;
			sh:maxlength 500 ;
			sh:minCount 1 ;
			sh:maxCount 1 ;
		] ;	
		
		sh:property [
			sh:path rico:hasEndDate ;
			sh:nodeKind sh:BlankNode ;
			sh:minCount 1 ;
		] .
		
archvd:SingleDateShape
	a sh:NodeShape ; 
	sh:targetClass  rico:SingleDate ;
	sh:property [
		sh:path rico:normalizedDateValue ;
		sh:datatype xsd:date ;
		sh:minCount 1 ;
	] .			
```

---
