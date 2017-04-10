songs = {
	("Nickleback", "How You Remind Me"),
	("Led Zeppilin", "Whole Lotta Love"),
	("Mumford and Sons", "Winter Winds"),
	("Needtobreathe", "Washed By the Water"),
	("Nickleback", "Animals")
}

no_more_nickleback = [band for band in songs if band[0] != "Nickleback"]
print(no_more_nickleback)
	
# words = ['big', 'red', 'dog', 'ate', 'his', 'food']
# three_letters_words = [ word.title() for word in words if len(word) == 3 ] 
# print(three_letters_words)
