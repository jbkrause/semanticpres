from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper(
    "http://127.0.0.1:9999/blazegraph/sparql"
)
sparql.setReturnFormat(JSON)

sparql.setQuery("""
    PREFIX rico: <https://www.ica.org/standards/RiC/RiC-O_v0-2.html#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT DISTINCT * WHERE {
      ?sub rico:title ?obj 
    } 
    LIMIT 100
    """
)

try:
    ret = sparql.queryAndConvert()

    for r in ret["results"]["bindings"]:
        print(r)
except Exception as e:
    print(e)