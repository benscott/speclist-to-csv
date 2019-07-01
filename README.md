# Speclist to CSV

Converts the UniProt speclist.txt (https://www.uniprot.org/docs/speclist.txt) to CSV file.


Input (speclist.txt):

```
ABEMA E  183220: N=Abelmoschus manihot
                 C=Sweet hibiscus
                 S=Hibiscus manihot
```

Output (speclist.csv): 

```
code,kingdom,taxon_node,scientific_name,common_name,synonym
ABEMA,E,183220,Abelmoschus manihot,Sweet hibiscus,Hibiscus manihot
```

## Usage

python main.py
