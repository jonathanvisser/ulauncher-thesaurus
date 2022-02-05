# -*- coding: utf-8 -*-
import json
import requests


URL_MASK = 'http://words.bighugelabs.com/api/2/{1}/{0}/json'
RELATIONSHIP_ABBR = {'syn':'Synonyms','ant':'Antonyms','rel':'Related terms','sim':'Similar terms','usr':'User suggestions'}

class BHTSearch():
  def __init__(self, params, api_key):
    self.key = params
    self.api = api_key

  def lookup_word(self,key):

    url = URL_MASK.format(key, self.api)

    r = requests.get(url)
    j = json.loads(r.text)
    return j
  def sizeFragments(self, results, wordtype,aWords,key,imagePath):
    # loop through array
    iRunningTotal = 0
    h = 0
    firstTimeFlag = True
    for i in range(0,len(aWords)):

      # count letters in word
      iRunningTotal = iRunningTotal + len(aWords[i])
      # if running total > 80 then create fragment array
      if (iRunningTotal > 30) or (i == len(aWords)-1):
        #print("h: " + str(h) + "   i: " + str(i))
        if firstTimeFlag == True:
          #print("FIRST TIME:")
          #print(aWords[h:i+1])
          self.addResult(results, wordtype,aWords[h:i+1],key,imagePath)
          firstTimeFlag = False
        else:
          imagePath = "images/blank.png"
          key =""
          wordtype = ""
          self.addResult(results, wordtype,aWords[h:i+1],key,imagePath)
          #print(aWords[h:i+1])
        h = i + 1
        iRunningTotal = 0
    

  def addResult(self, results, wordtype,words,key,imagePath):
    if key != "":
      key = RELATIONSHIP_ABBR[key]
    words = ', '.join(words)
    results.append({
      "name": "{}{}".format(wordtype,words),
      "description": "{}".format(key),
      "icon": imagePath
    })

  # A function named query is necessary, we will automatically invoke this function when user query this plugin
  def search(self):
    key = self.key
    if len(key) > 2:
      results = []
      rex = self.lookup_word(key) # thesaurus Rex... geddit!?! :D
      # take the result set and break it up into result sets to append
      for key, value in rex.items(): # loop through word types
        previouswordtype = ""
        wordtype = key.upper() + ": "
        imagePath = "images/syn.png"
        for key, value in value.items(): # for each word type there maybe syn, ant, rel, sim, and user defined words
          words = value #', '.join(value)
          if previouswordtype == wordtype:
            wordtype = ""
            imagePath = "images/" + key + ".png"
          self.sizeFragments(results, wordtype,words,key,imagePath)

          #results.append({
          #  "Title": "{}{}".format(wordtype,words),
          #  "SubTitle": "{}".format(RELATIONSHIP_ABBR[key]),
          #  "IcoPath": imagePath
          #})
          previouswordtype = wordtype

      return results
