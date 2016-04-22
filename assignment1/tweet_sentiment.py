# Purpose: to calcuate scores for each tweets based on scores file for selected words (AFINN-111.txt). If word in the tweets is not 
# the file, then the word for that score is 0
import json
import sys

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

# command line: python tweet_sentiment.py AFINN-111.txt output1.json
def main():
    sent_file = open(sys.argv[1]) # open the second file in the command line AFINN-111.txt
    tweet_file = open(sys.argv[2]) # open the third file in the command line coutput1.json

# Thought process: (back-forward process) 
## find out if the word in each tweet exists in the scores file, if yes, add sum scores
## involves two files: scores file and tweet file with json type
## convert json file to python data structures (dictionary) using json.loads

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
