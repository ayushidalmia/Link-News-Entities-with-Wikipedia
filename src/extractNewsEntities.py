#This script takes as input the news titles and extract the entites from them

#import packages
import ner

#initialise
data=[] 
location=[]
tagger = ner.SocketNER(host='localhost', port=8080)

#read the file containing news titles
with open('NewsTitle.txt', 'r') as f:
    for line in f:
        words=line.strip().split('\t')
        if len(words)==2:
            newsId=words[0]
            print newsId
            title=words[1]
            #get all entities for the title
            temp= tagger.get_entities(title)
            if temp:
                data.append(newsId.encode('utf-8')+"\t")
                for key in temp:
                    entityValue=temp[key]
                    for i in range(0,len(entityValue)):
                        data.append(entityValue[i].encode('utf-8')+",")
                    #find the entities which belong to class location
                    if key.encode('utf-8')=='LOCATION':
                        location.append(newsId.encode('utf-8')+"\t")
                        for i in range(0,len(entityValue)):
                            location.append(entityValue[i].encode('utf-8')+",")
                        location.append("\n")
                data.append("\n")
                                 
f.close()

#write the entities for each news title
f=open('NewsTitleEntities.txt', 'w')
f.write("".join(data))
f.close()

#write the location for each news title
f=open('NewsLocation.txt', 'w')
f.write("".join(location))
f.close()
