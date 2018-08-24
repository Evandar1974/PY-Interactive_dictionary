
import json
data = json.load(open("data.json"))

def translate(word):
	if word.lower() in data:
		return data[word]
	else:
		return "The word does not exist please check it."

word = input("Enter word: ")

print(translate(word))
