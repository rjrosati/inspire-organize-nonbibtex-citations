import urllib.request
import json
import time
from datetime import datetime
import os
from sys import platform
import subprocess
import argparse
import re



# basically, should take the latex file
# find all citation commands
# find all bibitems
# re-order bibitems to match
# fetch missing bibitems from inspire if they look like inspire format
texfile = 'slow-torsion_v11.tex'
citation_format = 'latex-eu'

citations = []
with open(texfile,'r') as f:
    for line in f:
        if '\\cite' in line:
            for match in re.finditer(r'\\cite',line):
                citestart = match.end() + 1
                if not any([c == '%' for c in line[:citestart]]):
                    citeend = line[citestart:].find('}') + citestart
                    for citation in line[citestart:citeend].split(','):
                        if citation.strip() not in citations:
                            citations.append(citation.strip())

print(f"Found {len(citations)} distinct cited works in the latex file.")
print(citations)

bibitems = []

print(f"The bibliography contains {len(bibitems)} works")
print(f"{}/{} are referenced in the text, and {} are missing.")

print("Querying INSPIRE for the missing entries...")

for citation in missing_citations:
        url = f'https://inspirehep.net/api/literature?sort=mostrecent&size=25&page=1&q=exactauthor%3A{paper_id}&format={citation_format}'


