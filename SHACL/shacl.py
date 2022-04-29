#!/usr/bin/env python3

from pyshacl import validate

import sys

if not len(sys.argv)==2:
    print('syntax: python shacl_validator.py <filename.ttl>')

shapes_file = open('shacl.ttl', 'r').read()
shapes_file_format = 'turtle'

data_file = open(sys.argv[1], 'r').read()
data_file_format = 'turtle'

conforms, v_graph, v_text = validate(data_file, shacl_graph=shapes_file,
                                     data_graph_format=data_file_format,
                                     shacl_graph_format=shapes_file_format,
                                     inference='rdfs', debug=True,
                                     serialize_report_graph=True)
#print(conforms)
print(v_graph.decode('utf-8'))
print(v_text)
