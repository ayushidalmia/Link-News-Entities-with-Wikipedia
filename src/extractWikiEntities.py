#This script takes as input the wikipedia dump and extracts the entities from
#the dump. The url of the corresponding entity can be derived from the
#entity name

data=[]

#read the wikipedia dump
f=open("enwiki-latest-pages-articles.xml","r")
for line in f:
    if "<page>"in line:
        while("</page>") not in line:
            line=f.next()
            if "<redirect title=" in line:
                line=(line.split("<redirect title=\"")[1]).split(" />")[0][:-1]
                title=line
                break;
            if "<title>" in line:
                line=(line.split("<title>")[1]).split("</title>")[0]
                title=line
        data.append(title)
f.close()

#write the entities
f=open("wikiEntitiesProcessed.txt","w")
f.write("\n".join(data))
f.close()
        
