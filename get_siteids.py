#script to get siteids for buildings
from sys import argv

script, filename = argv

code_lookup = {}

with open(filename) as f:
    for line in f:
        things = line.strip().split("//")
        code_lookup[things[0]] = things[1]

print(code_lookup)
            
