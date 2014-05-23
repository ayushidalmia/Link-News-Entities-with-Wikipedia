#This scripts takes as input the wikipedia dump and the newsfeed dump and returns
#the entity linkage for each news title in the given format.

execfile("extractWikiEntities.py")
execfile("disambiguousWikiEntities.py")
execfile("extractNewsFeed.py")
execfile("extractNewsEntities.py")
execfile("entityMapping.py")
execfile("compile.py")

