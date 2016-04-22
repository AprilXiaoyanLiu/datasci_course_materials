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
    
# convert affinn file to dictionary
    scores = {} # initialize an empty dictionary
    for line in sent_file:
    	term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
    	scores[term] = int(score)  # Convert the score to an integer.
    
    for i in range(len(twitterlist)):
    	if "text" in twitterlist[i]:
    		tweetword = twitterlist[i]["text"].split()
    		sentiment_score = 0
    		for word in tweetword:
    			if word in scores:
    				sentiment_score = sentiment_score + scores[word]
    		print sentiment_score
    
if __name__ == '__main__':
	main()