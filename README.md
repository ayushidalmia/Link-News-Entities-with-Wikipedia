Link-News-Entities-with-Wikipedia
=================================

This repository consists of the project done as part of the course Statistical Methods in AI- Monsoon 2013. The course was instructed by [Dr. Manish Gupta](http://research.microsoft.com/en-us/people/gmanish/)

A detailed report is available <a href="https://drive.google.com/file/d/0B87x7EOOS4ztVUYtbVQ1WG9OdVE/edit?usp=sharing",target="blank">here</a>

##Requirements

The code uses Python Version 2.7 along with the modules beautifulsoup, os, collections and ner. 

##Problem  Statement
The news feed crawled from various news websites for half a month (June 1-15, 2012) along with the Wikipedia dump is provided. It is aimed to link entities in News Feeds with Wikipedia entity pages using the title of the news.


###Instructions

Run the script entityLinkage.py

###Output  
The desired file entityLinkage.txt is generated along with other intermediate text files, the details of which are described below.

###Details  
The script entityLinkage.py executes six scripts. They are as follows:
 
* extractWikiEntities.py  
This corresponds to Step 1 of the methodology.  
**Input-** Wikipedia Dump (given as input)  
**Output-** wikiEntitiesProcessed.txt (It contains all the entities of Wikipedia extracted from the title)

* disambiguousWikiEntities.py  
This corresponds to Step 2 of the methodology.  
**Input-** wikiEntitiesProcessed.txt (generated from the previous step)  
**Output-** wikiEntitiesDisambiguity.txt(It contains the final entities from Wikipedia page after removing disambigous pages)

* extractNewsFeed.py  
This corresponds to Step 3 of the methodology.  
**Input-** news feed (given as input)  
**Output-** NewsData.txt (It contains newsId, file from which news is takes, news title, timestamp, author and url of the news in a tab separated  format)  
			NewsTitle.txt (It contains the newsId and newsTitle)  
			NewsDescription.txt (It contains the newsId and the description of the news)

* extractNewsEntities.py  
This corresponds to Step 4 of the methodology.  
**Input-** NewsTitle.txt(generated from the previous step)  
**Output-**NewsTitleEntities.txt (it contains the entites for each newsId separated by tab.Since each title may contain more than one entity,the entities are separated by comma)  
			NewsLocation.txt (it contains the location for each newsId)

* entityMapping.py  
This corresponds to Step 5 of the methodology.  
**Input-** WikiEntitiesDisambiguity.txt, newsTitleEntities.txt (generated earlier)  
**Output-** NewsWikiUrl.txt (it contains the newsId and the corresponding url for wikipedia)

* compile.py  
This corresponds to Step 6 of the methodology.  
**Input-** NewsTitleEntities.txt (generated earlier)  
			NewsWikiUrl.txt (generated earlier)  
			NewsLocation.txt (generated earlier)  
**Output-** entityLinkage.txt (it contains the final output file in the desired format)
