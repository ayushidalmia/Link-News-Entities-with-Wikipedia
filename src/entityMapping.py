#This script takes as input the entities of Wikipedia and Maps it to that of the
#newsfeed. Along with this, it also finds the url of the corresponding entities

#import packages
from collections import defaultdict

#initialisation
wikiEntities=defaultdict(int)
data=[]
count=0
present=0

#Read wikipedia entities
with open('wikiEntitiesDisambiguity.txt','r') as f:
    for line in f:
        wikiEntities[line.strip()]=1
f.close()

#Read newsfeed entities and map the wikipedia url
#The wikipedia url is generated from the wikipedia entities itself
with open('NewsTitleEntities.txt','r') as f:
    for line in f:
        words=line.strip().split('\t')
        newsId=words[0]
        print newsId
        listOfEntities=words[1]
        listOfEntities=listOfEntities.split(',')
        count=count+len(listOfEntities)-1
        for i in range(0,len(listOfEntities)-1):
            if wikiEntities[listOfEntities[i]]==1:
                present+=1
                entity=listOfEntities[i].replace(" ","_")
                url="en.wikipedia.org/wiki/"+entity
                data.append(newsId+"\t"+url+",")
                
#write the urls for the corresponding news title
f=open('NewsWikiUrl.txt', 'w')
f.write("\n".join(data))
f.close()

#Number of entities present in newsfeed
print count
#Number of entities found in wikipedia
print present
