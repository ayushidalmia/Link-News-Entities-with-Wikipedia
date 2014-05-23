#This script basically compiles everything from other files and generates the desired output file

#Initialise dictioaries
newsEntities={}
newsWikiUrl={}
newsLocation={}

#Read News Title Entities into dictionary into the corresponding dictionary
with open('NewsTitleEntities.txt','r') as f:
    for line in f:
        line=line.strip().split('\t')
        newsEntities[line[0]]=line[1]
    f.close()

#Read News Title Entities' corresponding Wikipedia Page's Urls into the corresponding dictionary
with open('NewsWikiUrl.txt','r') as f:
    for line in f:
        line=line.strip().split('\t')
        newsWikiUrl[line[0]]=line[1]
    f.close()

#Read Location derived from the news title into the corresponding dictionary
with open('NewsLocation.txt','r') as f:
    for line in f:
        line=line.strip().split('\t')
        newsLocation[line[0]]=line[1]
    f.close()


data=[]
count=0

#Read the data extracted from the news dump and append the news entities, location and Wikipedia Url
with open('NewsData.txt','r') as f:
    for line in f:
        line=line.strip().split('\t')
        if len(line)==6 and line[2]!="":
            newsId=line[0]
            print newsId
            newsFolder=line[1]
            newsTitle=line[2]
            newsTimeStamp=line[3]
            newsAuthor=line[4]
            newsUrl=line[5]
            if newsTimeStamp=="":
                newsTimeStamp="NULL"
            if newsAuthor=="":
                newsAuthor="NULL"
            if newsUrl=="":
                newsUrl="NULL"
            nEntities="NULL"
            nWikiUrl="NULL"
            nLocation="NULL"
            if newsId in newsEntities.keys():
                nEntities=newsEntities[newsId]
            if newsId in newsWikiUrl.keys():
                nWikiUrl=newsWikiUrl[newsId]
            if newsId in newsLocation.keys():
                nLocation=newsLocation[newsId]
            
            data.append(newsFolder+"\t"+newsTitle+"\t"+nEntities+"\t"+nWikiUrl+"\t"+newsTimeStamp+"\t"+nLocation+"\t"+newsAuthor+"\t"+newsUrl)
        else:
            count+=1
    f.close()

#write into final file
f=open('entityLinkage.txt','w')
f.write("\n".join(data))
f.close()

print count
