#!/usr/bin/python3

import os

files = os.listdir()

html_command = 'pandoc -t revealjs -s -o {fout} {fin} -V revealjs-url=reveal.js -V theme=white --katex'
#pdf_command = 'pandoc -t html5 -o {fout} {fin}'
pdf_command = 'pandoc -o {fout} {fin} -V colorlinks=true -V linkcolor=blue -V urlcolor=red -V toccolor=gray'


for f in files:
    if f.endswith('.md'):
        f2 = f[:-3]
        cmd = html_command.format(fin=f, fout=f2+'.html')
        print(cmd)
        os.system( cmd )
        
for f in files:
    if f.endswith('.md'):
        f2 = f[:-3]        
        cmd = pdf_command.format(fin=f, fout=f2+'.pdf')
        print( cmd )
        os.system( cmd )
