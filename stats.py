def find_words(text):
        words = text.split()
        count = len(words)
        return (count)

def letter_count(text):
	count = {}
	for letter in text.lower():
		if letter in count:
			count[letter] +=1
		else:
			count[letter] = 1
	return(count)

def sorting(count):
	return count["num"]

def convert(letter_count):
	char_list = []

	for letter in letter_count:
		letter_dict = {"char": letter, "num": letter_count[letter]}
		char_list.append(letter_dict)


	char_list.sort(reverse=True, key=sorting)
	return char_list
