#This script takes as input the entities extracted from the WikiDump and removes
#those entities which are redirected to disambiguity pages.

data=[]

with open('wikiEntitiesProcessed.txt', 'r') as f:
    for line in f:
        if '(disambiguation)' in line:
            continue
        data.append(line)
f.close()

f=open('wikiEntitiesDisambiguity.txt','w')
f.write("".join(data))
f.close()
        
