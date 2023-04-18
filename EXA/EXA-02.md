---
author: "Jan Krause-Bilvin"
title: "HEG-796-22-EXA-2"
subtitle: "Questions d'examen"
date: 2023-04-18
lang: fr-CH
encoding: utf-8
presention: "pandoc -t revealjs -s -o EXA.html EXA.md -V revealjs-url=reveal.js -V theme=white --katex; pandoc -t html5 -o 030-tp.pdf 030-tp.md"
---

# Question 2 : LDP et Python

Expliquer et commenter le code Python ci-dessous:

```
import requests
url = 'http://localhost:8080/rest/records/acv/D9999'
headers = {"Content-Type": "text/turtle"}
auth = ('fedoraAdmin', 'fedoraAdmin')
data = """ <>  <rico:title>            'Ceci est le titre'.
		   <>  <rico:scopeAndContent>  'Voilà la description'.
		   """
r = requests.put(url, auth=auth, data=data.encode('utf-8'), headers=headers)
print( 'Status:', r.status_code )
print( r.text )
```

---
