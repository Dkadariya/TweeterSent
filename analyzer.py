from elasticsearch import Elasticsearch
import requests
import json
es = Elasticsearch()
ncount=0
pcount=0
neucount=0
count1=0
count=0
total=0
def nonPhr():
	i = es.search('sentiment', 'test-type', body={
	  "size": 0,
	  "aggs": {
	    "group_by_nounPhrase": {
	      "terms": {
	        "field": "nounPhrase",
	        "size": 11
	      }
	    }
	  }
	})
	#data = json.dumps(i,indent=4)
	i = i['aggregations'] ['group_by_nounPhrase'] ['buckets'] 
	word=[]
	word_n = []
	count=[]
	count_n=[]
	merged=[]
	for value in i:
		word.append(value['key'].encode('utf-8'))
		count.append(value['doc_count'])
	#print word,count
	merged.append('noun')
	for x in xrange(1,10):
		word_n.append(word[x])
		count_n.append(count[x])

	merged.append(word_n)
	merged.append(count_n)
	print merged
	return merged

def queryS(text):
	i = es.search('sentiment', 'test-type', body={
	    "query" : {
	        "match" : {"sentiment":text}
	    },
	    "from":1,
	    "size":108966
	})
	Ftweets=['tweets']
	for tweet in i['hits']['hits']:
		pack = []
		pack=[tweet['_source']['username'],tweet['_source']['tweet']]
		Ftweets.append(pack)
	return Ftweets


def queryT(text):
	i = es.search('sentiment', 'test-type', body={
		    "query" : {
		        "match": { "tweet": text }
		    },
		    "from":1,
		    "size":108966
		})
	Stweets = ['tweets']
	for tweets in i['hits']['hits']:
		spack = []
		spack=[tweets['_source']['username'],tweets['_source']['tweet']]
		Stweets.append(spack)
	return Stweets

def scount():
	i = es.search('sentiment', 'test-type', body={
		    "query" : {
		        "match_all": {}
		    },
		    "from":1,
		    "size":108966
		})
	for tweets in i['hits']['hits']:
		sentiment=tweets['_source']['sentiment']
		if sentiment == 'positive':
			global pcount
			pcount+=1
		elif sentiment== 'negative':
			global ncount
			ncount +=1
		else:
			global neucount
			neucount +=1
		pol = float(tweets['_source']['polarity'])
		global total
		total = total + pol
	avg = total/108966
	fields=['positive','neutral','negative']
	scnt = [pcount, neucount, ncount,]
	data = ['scount',avg,fields,scnt]
	return data


def Savg():
	sav=["avg"]
	i = es.search('sentiment', 'test-type', body={
		    "query" : {
		        "match_all": {}
		    },
		    "from":1,
		    "size":128003
		})
	for tweets in i['hits']['hits']:
		pol = float(tweets['_source']['polarity'])
		global total
		total = total + pol
	avg = total/128004
		
	sav.append(avg)
	print sav
	return sav

	
#queryT("happy")
#nonPhr()
#queryS("positive")
#scount()
#Savg()
