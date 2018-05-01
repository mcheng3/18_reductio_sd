f = open("flatland.txt", "r")
text = f.read()
text_words = text.split()
text_words = [x.lower() for x in text_words]
# words
def word_freq(word, text_list):
	return reduce(lambda a, b: a + 1 if b == word else a, text_list, 0)
print "# of 'polygon's : " + str(word_freq('polygon', text_words))
print "# of 'dimensions's : " + str(word_freq('dimensions', text_words))

def words_freq(words, text_list):
	return reduce(lambda a, b: a + 1 if b in words else a, text_list, 0)
print "# of 'polygon's and 'dimension's : " + str(words_freq(['polygon', 'dimensions'], text_words))
print "# of 'the's, 'a's, and 'an's : " + str(words_freq(['a', 'an', 'the'], text_words))


