f = open("flatland.txt", "r")
text = f.read()
text_words = text.split()
text_words = [x.lower() for x in text_words]
f.close()
# words
def word_freq(word, text_list):
	return reduce(lambda a, b: a + 1 if b == word else a, text_list, 0)
print "# of 'polygon's : " + str(word_freq('polygon', text_words))
print "# of 'dimensions's : " + str(word_freq('dimensions', text_words))

#Expects two lists of words, returns the number of occurences of the former in the latter
def words_freq(words, text_list):
	return reduce(lambda a, b: a + 1 if b in words else a, text_list, 0)
print "# of 'polygon's and 'dimension's : " + str(words_freq(['polygon', 'dimensions'], text_words))
print "# of 'the's, 'a's, and 'an's : " + str(words_freq(['a', 'an', 'the'], text_words))

#Returns THE most frequent word
def most_freq(text_list):
	uniqueWords = [text_list[i] for i in range(len(text_list)) if i == text_list.index(text_list[i])]
	all_freqs = [word_freq(w, text_list) for w in uniqueWords]
	biggest_freq = reduce(lambda currentMax, freq: freq if freq > currentMax else currentMax, all_freqs, 0)
	return uniqueWords[ all_freqs.index(biggest_freq) ]
print "most frequent word: " + most_freq(text_words)
