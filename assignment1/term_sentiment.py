''' first methodology: define sentiment metric score as positive_count/neg_count but the result is not correct'''

'''first methodology''' 

import json
import sys

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    twitterlist = []  # Create list with dictionary
    for line in tweet_file:
    	line = line.encode('utf-8')
    	twitterlist.append(json.loads(line)) 
    
    scores = {} # initialize an empty dictionary
    for line in sent_file:
    	term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
    	scores[term] = int(score)  # Convert the score to an integer.
    
    scores_others_pos = {}
    scores_others_neg = {}
    for i in range(len(twitterlist)):
    	if "text" in twitterlist[i]:
    		tweetword = twitterlist[i]["text"].split()
    		count_pos = 0
    		count_neg = 0
    		for word in tweetword:
    			word = word.encode('utf-8')
    			if word in scores:
    				if scores[word] > 0:
    					count_pos = count_pos + 1
    				elif scores[word] < 0:
    					count_neg = count_neg + 1
    		for word in tweetword:	
    			word = word.encode('utf-8')
    			if word not in scores:
    				if word not in scores_others_pos:
    					scores_others_pos[word] = count_pos
    					scores_others_neg[word] = count_neg
    				else:
    					scores_others_pos[word] = scores_others_pos[word] + count_pos
    					scores_others_pos[word] = scores_others_neg[word] + count_neg
    				
	d = {}
	for key, val in scores_others_neg.items():
		if val is not 0:
			d[key] = float(scores_others_pos[key])/val
		elif val is 0:
			d[key] = float(scores_others_pos[key])
    		
    for k, v in d.items():
    	print k, float(v)
    
    		
    
if __name__ == '__main__':
	main()
	
'''second methodology: sentiment score definition is sourced from http://www.slideshare.net/faigg/tutotial-of-sentiment-analysis'''
'''for example, if the word 'football' exists in two tweets, the first tweet sentiment score is 5, the second tweet sentiment score is 1
then the sentiment score for the word 'football' should be (5+1)/2 = 3'''
'''to achieve this, my thought is to create two differnt dictionaries: one is senti_sore to store each word and their total score; another 
is the number of the tweets the word is in''' 

'''second methodology:'''
import json
import sys

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    twitterlist = []  # Create list with dictionary
    for line in tweet_file:
    	line = line.encode('utf-8')
    	twitterlist.append(json.loads(line)) 
    
    scores = {} # initialize an empty dictionary
    for line in sent_file:
    	term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
    	scores[term] = int(score)  # Convert the score to an integer.
    
    sent_score = {}
    count_number = {}
    for i in range(len(twitterlist)):
    	if "text" in twitterlist[i]:
    		tweetword = twitterlist[i]["text"].split()
    		sentscore = 0
    		for word in tweetword:
    			word = word.encode('utf-8')
    			if word in scores:
    				sentscore = sentscore + scores[word]
    		for word in tweetword:	
    			word = word.encode('utf-8')
    			if word not in scores:
    				if word not in sent_score:
    					sent_score[word] = sentscore
    					count_number[word] = 1
    				elif word in sent_score:
    					sent_score[word] = sentscore + sent_score[word]
    					count_number[word] = count_number[word] + 1
    				
    d = {}
    for key, val in sent_score.items():
	d[key] = float(val)/count_number[key]
    		
    for k, v in d.items():
    	print k, float(v)
    
    		
    
if __name__ == '__main__':
	main()
