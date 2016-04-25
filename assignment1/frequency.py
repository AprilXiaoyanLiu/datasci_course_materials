import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    
    tweet_file = open(sys.argv[1])

    twitterlist = []  # Create list with dictionary
    for line in tweet_file:
    	line = line.encode('utf-8')
    	twitterlist.append(json.loads(line)) 
    
    
    count_word = {}
    count_total = {}
    for i in range(len(twitterlist)):
    	if "text" in twitterlist[i]:
    		tweetword = twitterlist[i]["text"].split()
    		sentscore = 0
    		for word in tweetword:
    			word = word.encode('utf-8')
    			if word not in count_word:
    				count_word[word] = 1
    			elif word in count_word:
    				count_word[word] += 1
    			count_total[word] = sum(len(x) for x in tweetword if word in x)
    				
    d = {}
    for key, val in count_word.items():
	d[key] = val/count_total[key]
    		
    for k, v in d.items():
    	print k, float(v)
    
    		
    
if __name__ == '__main__':
	main()
