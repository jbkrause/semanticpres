---
author: "Jan Krause-Bilvin"
title: "HEG-796-22-EXA-6"
subtitle: "Questions d'examen"
date: 2023-04-18
lang: fr-CH
encoding: utf-8
presention: "pandoc -t revealjs -s -o EXA.html EXA.md -V revealjs-url=reveal.js -V theme=white --katex; pandoc -t html5 -o 030-tp.pdf 030-tp.md"
---

# Question 6 : SHACL - document et agent

---

Expliquer et commenter le code SHACL ci-dessous:

```
archvd:DocumentShape
	a sh:NodeShape ; 
	sh:targetClass  archvd:Document ;
		
		sh:property [
			sh:path rico:title;
			sh:datatype xsd:string ;
			sh:maxlength 500 ;
			sh:minCount 1 ;
			sh:maxCount 1 ;
		] ;	

		sh:property [
			sh:path rico:hasCreator ;
			sh:nodeKind sh:BlankNode ;
			sh:minCount 1 ;
		] ;
		
		sh:property [
			sh:path (rico:hasCreator rdf:type)  ;
			sh:targetSubjectOf rico:Agent ;
			sh:minCount 1 ;
		] .

archvd:AgentShape
	a sh:NodeShape ; 
	sh:targetClass  rico:Agent ;
	
	sh:property [
		sh:path rico:hasOrHadName;
		sh:datatype xsd:string ;
		sh:maxlength 500 ;
		sh:minCount 1 ;
		sh:maxCount 1 ;
	] ;
	
	sh:property [	
		sh:path rico:identifier;
		sh:minCount 1 ;
	] ;
	
	sh:property [
		sh:path rico:hasModificationDate ;
		sh:datatype xsd:date ;
		sh:minCount 1 ;
	] .		
```

---
