import json
import sys
import os


tweet_file = open(sys.argv[2])
sent_file = open(sys.argv[1])
twitterlist = []  # Create list with dictionary
for line in tweet_file:
    line = line.encode('utf-8')
    twitterlist.append(json.loads(line))
    
  
scores = {} # initialize an empty dictionary
for line in sent_file:
    term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
    scores[term] = int(score)

 
 


'''for tweet in twitterlist:
    	if "text" in tweet:
    		tweetword = tweet["text"].split()
    		sentiment_score = 0
    		for word in tweetword:
    			if word in scores:
    				sentiment_score = sentiment_score + scores[word]
    		print sentiment_score'''
    		
    		
'''parse out location data'''  		

location = {}	
count_loc = {}
for tweet in twitterlist:
	if "place" and "text" in tweet:
		tweetword = tweet["text"].split()
		sentiment_score = 0 
		for word in tweetword:
			if word in scores:
				sentiment_score = sentiment_score + scores[word]
	
		if tweet["place"] is not None:
			if tweet["place"]["country"] == "United States":
				loc = tweet["place"]["full_name"].encode('utf-8')
				city, state = loc.split(",")
				if state not in location:
					location[state] = sentiment_score
					count_loc[state] = 1
				elif state in location:
					location[state] += sentiment_score
					count_loc[state] += 1

d = {}
for key, val in location.items():
	d[key] = val/count_loc[key]

lst = list()		
for k, v in d.items():
    lst.append((float(v),k))

lst.sort(reverse=True)

for va, ke in lst[:1]:
	print ke

		#'''elif tweet["place"] is None:
			#if "user" in tweet:
				#if "location" in tweet["user"]:
					#key = tweet["user"]["location"]'''
			
			


		