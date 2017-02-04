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
path = os.path.join(os.path.dirname(__file__), 'ontologylistcomplete.txt')
terms_file = open(path, "r")
terms = []
for line in terms_file:
    terms.append(line)

# Do a search for every term

search_results = []   # creates a list of the search results
totalNumberOfLinks = 0
ontologyCount = 0

for term in terms:
    termstring = REST_URL + "/search?q=" + term
    search_results.append('The term is ' + term)
    for count in range(0,len(get_json(termstring)["collection"])):
      search_results.append(get_json(termstring)["collection"][count]["links"]["ontology"])
    #search_results.append(get_json(termstring))
    
# Print the results

num = 0
uniqueOntologyList = []
for result in search_results:
  if result not in uniqueOntologyList:
      uniqueOntologyList.append(result)
      print(num)
      print(result)
      num = num + 1     

print('The average number of links is ' + str(totalNumberOfLinks/ontologyCount))          