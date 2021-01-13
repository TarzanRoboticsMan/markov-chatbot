import json

file = open("data/sheeran.txt")

dict = {}


for line in file: #treats each line as individual
	words = line.split() #capitalization and punctation are "part of" the word
	for i in range(len(words)-1): #so last word doesnt get a value
		word = words[i]
		if word not in dict:
			dict[word] = {words[i+1]:1}
		else:
			occurences = dict[word]
			nextWord = words[i+1]
			if nextWord not in occurences:
				occurences[nextWord]=1
			else:
				occurences[nextWord]+=1


#"dog": [["hey",2],["fight",1]]
#"dog": {"hey":2, "fight":2}

print(json.dumps(dict))
