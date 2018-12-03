# SENTILYZER - MY TOY SENTIMENT ANALYZER:

# Any sample text as a tokenized list. 
sample="The question is witch which is which ?"
sample=sample.split(" ")
# Any list of known sentiment.
test=["which","witch"]
'''
sentilyze() iterates over the sample text, checking if a word in the sample is the list of known sentiment. 
'''

# def sentilyze(x,y):
# 	a=0 
# 	for w in x:
# 		if w in y:
# 			a+=1	
# 		else:
# 			pass
# 	print(a)
# sentilyze(sample,test)

# The method of tokenizing we did is super basic. We could make improvements tokenizing by 
# words/sentences with regular expressions. However, this is already done well by the module nltk. 


sample_text="So, we're going to try and tokenize these setences. This'll be hard to do from scratch."
from nltk.tokenize import sent_tokenize, word_tokenize
print(sent_tokenize(sample_text))

