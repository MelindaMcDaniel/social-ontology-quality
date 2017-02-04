import urllib2
import json
import os
from pprint import pprint

REST_URL = "http://data.bioontology.org"
API_KEY = "d8801e4d-b082-4150-b1dc-084f8390bfdb"

def get_json(url):
    opener = urllib2.build_opener()
    opener.addheaders = [('Authorization', 'apikey token=' + API_KEY)]
    result = json.loads(opener.open(url).read()) # produces a dictionary
    #print result.keys()
    return result 

# Get list of search terms
path = os.path.join(os.path.dirname(__file__), 'keywordlist.txt')
keywords_file = open(path, "r")
keywords = []
for keyword in keywords_file:
    keywords.append(keyword)

# Do a search for every  keyword
search_results = []   # creates a list of the search results
totalNumberOfLinksAltogether = 0
keywordCount = 0
maxkeywordLinkCount = 0

for keyword in keywords:
    keyword_results = []
    termstring = REST_URL + "/search?q=" +  keyword
    keyword_results.append('The keyword is ' +  keyword)  # search all ontologies for this word
    uniquekeywordList = []
    thiskeywordLinkCount = 0
    for count in range(0,len(get_json(termstring)["collection"])):
        result = get_json(termstring)["collection"][count]["links"]["ontology"]
        if result not in uniquekeywordList:
            uniquekeywordList.append(result)
            keyword_results.append(result)
            thiskeywordLinkCount += 1
    keyword_results.append(thiskeywordLinkCount)
    if thiskeywordLinkCount>maxkeywordLinkCount:
        maxkeywordLinkCount=thiskeywordLinkCount
    for item in keyword_results:
        print(str(item) + ','),  # prints all lines of the results as a csv file     
                
# Print the final results

#print('The maximum number of ontologies found is ' + str(maxkeywordLinkCount))    
         