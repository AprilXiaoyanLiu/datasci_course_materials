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
