#This script extracts the required data from the News feed dump given.
#It extracts newstitle, folder in which the title is present, author of the news,
#the timestamp when the news was written and the url of the news.

#imported packages
from os import listdir
from os.path import isfile, join
from bs4 import BeautifulSoup

count=0

#iterate each of the 15 folders (stands for each day in the month)
for i in range(1,16):
    
    data=[]
    newstitle=[]
    newsdescription=[]

    #set path to traverse news files in each directory
    if i<10:
        path="news\2012060"+str(i)
        folder="2012060"
    else:
        path="news\201206"+str(i)
        folder="201206"   
    files=listdir(path)

    #Read each file in each folder 
    for newsfile in files:        
        if "associatedpress" in newsfile or "huffingtonpost" in newsfile or "usatoday" in newsfile:
            continue        
        filename = path+"/"+newsfile
        soup = BeautifulSoup(open(filename),"xml")
        for news in soup.find_all("item"):
            
            print count
            count+=1

            #initialise
            title=""
            author=""
            link=""
            desc=""
            timeStamp=""

            #write the atribute values if they exist
            if news.title:
                title=news.title.text.strip().encode('utf-8')
            if news.find("creator"):
                author=news.find("creator").text.strip().encode('utf-8')
            if news.pubDate:
                timeStamp=news.pubDate.text.strip().encode('utf-8')
            if news.link:
                link=news.link.text.strip().encode('utf-8')
            if news.description:
                desc=news.description.text.strip().encode('utf-8')

             
            data.append(str(count)+"\t"+folder+str(i)+"/"+newsfile+"\t"+title+"\t"+timeStamp+"\t"+author+"\t"+link)
            newstitle.append(str(count)+"\t"+title)
            newsdescription.append(str(count)+"\t"+desc)
         
            
    
    #write newsid, newstitle, folder in which the title is present, author of the news
    #the timestamp when the news was written and the url of the news.
    f=open("NewsData.txt","a")
    f.write("\n".join(data))
    f.close()

    #write the news id and the corresponding newstitle
    f=open("NewsTitle.txt","a")
    f.write("\n".join(newstitle))
    f.close()

    #write the news id and the corresponding description
    f=open("NewsDescription.txt","a")
    f.write("\n".join(newsdescription))
    f.close()
    
