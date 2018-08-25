
import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
	if word.lower() in data:
		return data[word]
	elif len(get_close_matches(word, data.keys())) > 0:
		yn = input("Did you mean %s instead? please enter Y or N: " % get_close_matches(word, data.keys())[0]).upper
		if yn == "Y":
			return data[get_close_matches(word, data.keys())[0]]
		elif yn == "N":
			return "The word doesnt exist. please double check it"
		else:
			return "We didnt understand your entry."

	else:
		return "The word does not exist please check it."


word = input("Enter word: ")

print(translate(word))
