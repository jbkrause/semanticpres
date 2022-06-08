# Source

https://github.com/blazegraph/database/wiki/Quick_Start

# Run

``` bash

java -server -Xmx4g -jar blazegraph.jar
```

serviceURL: http://127.0.0.1:9999

# Upload

tab: UPDATE

    Type: RDF Data
    Format Turtle
    
    
# Query

PREFIX rico: <https://www.ica.org/standards/RiC/ontology#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT DISTINCT ?pred WHERE {
  ?sub ?pred ?obj .
  FILTER(regex(str(?pred), "RiC" ) )
} 
LIMIT 100

PREFIX rico: <https://www.ica.org/standards/RiC/ontology#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT DISTINCT * WHERE {
  ?sub ?pred ?obj .
  FILTER(regex(str(?pred), "RiC.*#title" ) )
} 
LIMIT 100


PREFIX rico: <https://www.ica.org/standards/RiC/ontology#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT DISTINCT * WHERE {
  ?sub <https://www.ica.org/standards/RiC/RiC-O_v0-2.html#title> ?obj 
} 
LIMIT 100

### List titles

PREFIX rico: <https://www.ica.org/standards/RiC/RiC-O_v0-2.html#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT DISTINCT * WHERE {
  ?sub rico:title ?obj 
} 
LIMIT 100

### RECURSIVE patterns

PREFIX rico: <https://www.ica.org/standards/RiC/RiC-O_v0-2.html#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT DISTINCT * WHERE {
  <https://data.archivescommunales.ch/object/001228-4-PP060-A-01-04> rico:isOrWasPartOf* ?obj .  
} 
LIMIT 100


### RECURSIVE patterns

PREFIX rico: <https://www.ica.org/standards/RiC/RiC-O_v0-2.html#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT DISTINCT * WHERE {
  <https://data.archivescommunales.ch/object/001228-4-PP060> ^rico:isOrWasPartOf* ?obj .  
} 
LIMIT 100


PREFIX rico: <https://www.ica.org/standards/RiC/RiC-O_v0-2.html#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT DISTINCT * WHERE {
  ?sub rico:title ?obj .
  FILTER(regex(str(?obj), ".*[Hh][oô]tel.*" ) )
} 
LIMIT 100


PREFIX rico: <https://www.ica.org/standards/RiC/RiC-O_v0-2.html#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT DISTINCT * WHERE {
  ?sub rico:title ?obj .
  FILTER(regex(str(?obj), ".*[Hh][oô]tel.*" ) )
} 
LIMIT 100

PREFIX rico: <https://www.ica.org/standards/RiC/RiC-O_v0-2.html#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT DISTINCT * WHERE {
  ?record rico:title ?title .
  ?record rico:isAssociatedWithDate/rico:expressedDate ?date .
  FILTER(regex(str(?title), ".*[Hh][oô]tel.*" )) .
  FILTER(regex(str(?date) , ".*19[34]\\d*"     )) .
} 
LIMIT 100