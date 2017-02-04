import urllib2
import json
import os

REST_URL = "http://data.bioontology.org"
API_KEY = "d8801e4d-b082-4150-b1dc-084f8390bfdb"

def get_json(url):
    opener = urllib2.build_opener()
    opener.addheaders = [('Authorization', 'apikey token=' + API_KEY)]
    result = json.loads(opener.open(url).read()) # produces a dictionary
    #print result.keys()
    return result 

# Get list of search terms
path = os.path.join(os.path.dirname(__file__), 'ontologylistcomplete.txt')
ontologies_file = open(path, "r")
ontologies = []
for ontology in ontologies_file:
    ontologies.append(ontology)

# Do a search for every ontology
#search_results = []   # creates a list of the search results
#totalNumberOfLinksAltogether = 0
ontologyCount = 0
#maxOntologyLinkCount = 0
#listOfLinkCounts = []
csvlist= []

for ontology in ontologies:   # takes too long to run - needs to be divided into parts
    ontologyCount = ontologyCount + 1
    #ontology_results = []
    termstring = REST_URL + "/search?q=" + ontology
    #ontology_results.append('The ontology is ' + ontology)  # search all other ontologies for this one
    uniqueOntologyList = []
    thisOntologyLinkCount = 0
    for count in range(0,len(get_json(termstring)["collection"])):
        result = get_json(termstring)["collection"][count]["links"]["ontology"]
        if result not in uniqueOntologyList:
            uniqueOntologyList.append(result)
            thisOntologyLinkCount = thisOntologyLinkCount + 1
            #totalNumberOfLinksAltogether = totalNumberOfLinksAltogether + 1
    #ontology_results.append("This ontology's link count: " + str(thisOntologyLinkCount))
    csvlist.append(ontology + ',' + str(thisOntologyLinkCount)),
    #listOfLinkCounts.append(thisOntologyLinkCount)
#    if thisOntologyLinkCount>maxOntologyLinkCount:
#        maxOntologyLinkCount=thisOntologyLinkCount
#    ontology_results.append("\n\n") 
    #for item in ontology_results:
        #print(item)  # prints all lines of the results           
                
# Print the final results
#listOfLinkCounts = sorted(listOfLinkCounts)
#for count in listOfLinkCounts:
    #print(count) 

#print('The average number of links is ' + str(totalNumberOfLinksAltogether/(ontologyCount*1.0))) 
#print('The maximum number of links is ' + str(maxOntologyLinkCount))    

for item in csvlist:
    print(str(item) + ","),            