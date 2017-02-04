import urllib2
import json
import os
import csv

REST_URL = "http://data.bioontology.org"
API_KEY = "d8801e4d-b082-4150-b1dc-084f8390bfdb"

def get_json(url):
    opener = urllib2.build_opener()
    opener.addheaders = [('Authorization', 'apikey token=' + API_KEY)]
    result = json.loads(opener.open(url).read()) # produces a dictionary
    #print result[0]
    return result 

# Get list of ontologies
path = os.path.join(os.path.dirname(__file__), 'ontologylistcomplete.txt')
ontology_file = open(path, "r")
ontologies = []
for line in ontology_file:
    ontologies.append(line)

# Do a search for every ontology

search_results = []   # creates a list of the search results
totalNumberOfSubmissions = 0
ontologyCount = 0
maxSubmissions = 0
minSubmissions = 100
csvlist= []
#sumOfSquares = 0
#listOfLinkCounts = []

for ontology in ontologies:   
    ontologystring = REST_URL + "/ontologies/" + ontology.rstrip() + "/submissions"
    # print ontology name
    search_results.append('The ontology is ' + ontology)
    for count in range(0,1):  # the first one is the most recent
      #search_results.append(get_json(termstring)["collection"][count]["links"]["ontology"])
      try:
          numberOfSubmissions = int(get_json(ontologystring)[0]['submissionId'])
          totalNumberOfSubmissions += numberOfSubmissions
          ontologyCount += 1
          search_results.append('Number of submissions: ' + str(numberOfSubmissions))
          #listOfLinkCounts.append(numberOfSubmissions)
          normalizedSubmissions = (numberOfSubmissions - 1)/560.0
          search_results.append('Normalized number of submissions: ' + str(normalizedSubmissions))
          #sqrOfDifference = (30.182 - numberOfSubmissions)**2
          #sumOfSquares += sqrOfDifference
          # take this out later
          #temp = (numberOfSubmissions/30.182)   # average number of submissions as of 1/19/2016
          #print temp
          #search_results.append('History metric result:' + str(temp))
          # check for max and min
          if numberOfSubmissions > maxSubmissions:
              maxSubmissions = numberOfSubmissions
          if numberOfSubmissions < minSubmissions:
              minSubmissions = numberOfSubmissions 
          csvlist.append(ontology)
          csvlist.append(numberOfSubmissions)     
              
          # compute years of Submissions
          try:
              yearsOfSubmissions = int(get_json(ontologystring)[0]['released'][0:4]) - int(get_json(ontologystring)[numberOfSubmissions-1]['submissionId'])
              year1 = int(get_json(ontologystring)[0]['released'][0:4])
              yearLast = int(get_json(ontologystring)[numberOfSubmissions-1]['released'][0:4])
              search_results.append('Year of first submission: ' + str(yearLast))
              search_results.append('Year of last submission: ' + str(year1))
              search_results.append('Total history in years: ' + str(year1 - yearLast + 1))
          except Exception:
              search_results.append('unable to locate years of submissions')
      except Exception:
          search_results.append('unable to locate number of submissions')
      
      search_results.append('\n\n')
# Print the results

#for result in search_results:
    #print(result)

#listOfLinkCounts = sorted(listOfLinkCounts)
#for count in listOfLinkCounts:
    #print(count)
    
print('The average number of revisions is ' + str(totalNumberOfSubmissions/(ontologyCount*1.0)))
print('The maximum number of revisions is ' + str(maxSubmissions))    
print('The minimum number of revisions is ' + str(minSubmissions))
# compute standard deviation
#stdDeviation = (sumOfSquares / (ontologyCount - 1))**.5
#print('The standard deviation is ' + str(stdDeviation)) 

for item in csvlist:
    print(str(item) + ","),

   
    
    

        
    