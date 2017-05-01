from elasticsearch import Elasticsearch
import requests
import json

es = Elasticsearch()
i = es.search('sentiment', 'test-type', body={
	    "query" : {
	        "match_all": {}
		    },
	    "from":1,
	    "size":128003
	})
interval=[]


count12=0
count18=0
count13=0
count14=0
count15=0
count16=0
count17=0	
for tweets in i['hits']['hits']:
	date=tweets['_source']['date']
	hour=date.split(' ')
	hour=hour[3].split(':')
	hr = int(hour[0])

	#print base_hr
	if(hr==12):
		count12+=1
	elif(hr==13):
		count13+=1
	elif(hr==14):
		count14+=1
	elif(hr==15):
		count15+=1
	elif(hr==16):
		count16+=1
	elif(hr==17):
		count17+=1
	elif(hr==18):
		count18+=1


value= [count12,count13,count14,count15,count16,count17,count18]
inter = ["12:00","13:00","14:00", "15:00", "16:00", "17:00", "18:00"]
interval=["Ttime",value,inter]

print interval