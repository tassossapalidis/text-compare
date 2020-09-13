from functools import reduce
from math import *

class TextModel:
	"""
	A statistical representation of a body of text, used to perform comparisons
	with other TextModels or text samples.
	"""
	def __init__(self, model_name):
		'''
		Constructor for TextModel object, defines empty dictionaries for 
		each comparison method.
		'''
		self.name = model_name
		self.words = {}
		self.word_lengths = {}
		self.stems = {}
		self.sentence_lengths = {}
		'''added feature: punctuation
		punctuation is a dictionary that records number of times each
		punctuation appears'''
		self.punctuation = {}
		'''added feature: stop words
		stop_words is a dictionary that records number of times each 
		stop_word appears'''
		self.stop_words = {} 

	def __repr__(self):
		"""
		Return a string representation of the TextModel.
		"""
		s  = 'text model name: ' + self.name + '\n'
		s += '  number of words: ' + str(len(self.words)) + '\n'
		s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
		s += '  number of stems: ' + str(len(self.stems)) + '\n'
		s += '  number of sentence lengths: ' + \
		str(len(self.sentence_lengths)) + '\n'
		s += '  number of punctuation marks: '+ \
		str(len(self.punctuation)) + '\n' 
		s += '  number of stop words: ' + str(len(self.stop_words))
		return s
	def save_model(self):
		'''Saves TextModel object self by writing its feature
		dictionaries to files '''
		wordsFile = self.name + '_' + 'words'
		lengthsFile = self.name + '_' + 'word_lengths'
		stemsFile = self.name + '_' + 'stems'
		sentence_lengthsFile = self.name + '_' + 'sentence_lengths' 
		punctuationFile = self.name + '_' + 'punctuation'
		stop_wordsFile = self.name + '_' + 'stop_words'

		f_words = open(wordsFile,'w')
		f_words.write(str(self.words))
		f_words.close()

		f_lengths = open(lengthsFile,'w')
		f_lengths.write(str(self.word_lengths))
		f_lengths.close()

		f_stems = open(stemsFile,'w')
		f_stems.write(str(self.stems))
		f_stems.close()

		f_sentence_lengths = open(sentence_lengthsFile,'w')
		f_sentence_lengths.write(str(self.sentence_lengths))
		f_sentence_lengths.close()

		f_punctuation = open(punctuationFile,'w')
		f_punctuation.write(str(self.punctuation))
		f_punctuation.close()

		f_stop_words = open(stop_wordsFile, 'w')
		f_stop_words.write(str(self.stop_words))
		f_stop_words.close()

	def read_model(self):
		'''Reads stored dictionaries for called TextModel object from
		their files and assigns them to the attributes of TextModel '''
		wordsFile = self.name + '_' + 'words'
		lengthsFile = self.name + '_' + 'word_lengths'
		stemsFile = self.name + '_' + 'stems'
		sentence_lengthsFile = self.name + '_' + 'sentence_lengths' 
		punctuationFile = self.name + '_' + 'punctuation'
		stop_wordsFile = self.name + '_' + 'stop_words'

		f_words = open(wordsFile,'r')
		words_string = f_words.read()
		f_words.close()
		self.words = dict(eval(words_string))

		f_lengths = open(lengthsFile,'r')
		lengths_string = f_lengths.read()
		f_lengths.close()
		self.word_lengths = dict(eval(lengths_string))

		f_stems = open(stemsFile,'r')
		stems_string = f_stems.read()
		f_stems.close()
		self.stems = dict(eval(stems_string))

		f_sentence_lengths = open(sentence_lengthsFile,'r')
		sentence_lengths_string = f_sentence_lengths.read()
		f_sentence_lengths.close()
		self.sentence_lengths = dict(eval(sentence_lengths_string))

		f_punctuation = open(punctuationFile,'r')
		punctuation_string = f_punctuation.read()
		f_punctuation.close()
		self.punctuation = dict(eval(punctuation_string))
		
		f_stop_words = open(stop_wordsFile,'r')
		stop_words_string = f_stop_words.read()
		f_stop_words.close()
		self.stop_words = dict(eval(stop_words_string))


	def add_string(self, s):
		"""
		Analyzes the string s and adds its pieces to all of the dictionaries
		in this text model.
		"""
		# Number of Words
		word_list = clean_text(s)

		for w in word_list:
			if w in self.words:
				self.words[w] += 1
			else:
				self.words[w] = 1

		# Word Stems
		for w in word_list:

			stemm = stem(w)

			if stemm in self.stems:
				self.stems[stemm] += 1
			else:
				self.stems[stemm] = 1

		# Word Lengths
		for w in word_list:

			length = len(w)

			if length in self.word_lengths:
				self.word_lengths[length] += 1
			else:
				self.word_lengths[length] = 1

		# Sentence Length
		sentence_list = sentence_split(s)
		for sentence in sentence_list:
			word_sentence_list = clean_text(sentence)
			sentence_length = len(word_sentence_list)

			if sentence_length == 0:
				pass
			elif sentence_length in self.sentence_lengths:
				self.sentence_lengths[sentence_length] += 1
			else:
				self.sentence_lengths[sentence_length] = 1

		# Punctuation
		punc_list = list(map(lambda x: chr(x), list(range(33,65)) + \
			list(range(91,97)) + list(range(123,128))))

		for char in s:
			if char in punc_list:
				if char in self.punctuation:
					self.punctuation[char] += 1
				else:
					self.punctuation[char] = 1

		# Stop words
		stop_words_list = ["ourselves", "hers", "between", "yourself", \
		"but","again", "there", "about", "once", "during", "out", "very", \
		"having", "with", "they", "own", "an", "be", "some", "for", "do", \
		"its", "yours", "such", "into", "of", "most", "itself", "other", \
		"off", "is", "am", "or", "who", "as", "from", "him", "each", \
		"the", "themselves", "until", "below", "are", "we", "these", \
		"your", "his", "through", "dont", "nor", "me", "were", "her", \
		"more", "himself", "this", "down", "should", "our", "their", \
		"while", "above", "both", "up", "to", "ours", "had", "she", \
		"all", "no", "when", "at", "any", "before", "them", "same", \
		"and", "been", "have", "in", "will", "on", "does", "yourselves",\
		"then", "that", "because", "what", "over", "why", "so", "can",\
		"did", "not", "now", "under", "he", "you", "herself", "has", "just", \
		"where", "too", "only", "myself", "which", "those", "i", "after", \
		"few", "whom", "being", "if", "theirs", "my", "against", "a", \
		"by", "doing", "it", "how", "further", "was", "here", "than"]

		for word in word_list:
			if word in stop_words_list and word in self.stop_words:
				self.stop_words[word] += 1
			elif word in stop_words_list:
				self.stop_words[word] = 1
			else:
				pass


	def add_file(self, filename):
		'''Adds all of the text in the file identified by filename
		to the TextModel given that input filename is name of file'''
		f = open(filename, 'r', encoding='utf8', errors = 'ignore')

		string = f.read()
		string = string.replace('\n','')

		self.add_string(string)

		f.close()

	def similarity_scores(self, other):
		'''Consumes another TextModel and computes and returns 
		a list of log similarity scores measuring the similarity 
		of self and other, one score for each type of feature'''
		word_score = compare_dictionaries(other.words,self.words)
		length_score = \
		compare_dictionaries(other.word_lengths,self.word_lengths)
		stem_score = compare_dictionaries(other.stems,self.stems)
		sentence_length_score = \
		compare_dictionaries(other.sentence_lengths,self.sentence_lengths)
		punctuation_score = \
		compare_dictionaries(other.punctuation,self.punctuation)
		stop_words_score = \
		compare_dictionaries(other.stop_words,self.stop_words)


		return [word_score,length_score,stem_score] + \
		[sentence_length_score,punctuation_score,stop_words_score]


	def classify(self, source1, source2):
		'''Consumes two other “source” TextModel objects (source1 and source2)
		 and returns which of those two TextModels is the more likely source 
		 of the called TextModel self'''
		scores1 = self.similarity_scores(source1)
		scores2 = self.similarity_scores(source2)

		weighted_sum1 = 10 * scores1[0] + 5 * scores1[1] + 7 * scores1[2] + \
		10 * scores1[3] + 5 * scores1[4] + 5 * scores1[5]

		weighted_sum2 = 10 * scores2[0] + 5 * scores2[1] + 7 * scores2[2] + \
		10 * scores2[3] + 5 * scores2[4] +  5 * scores2[5]

		maximum = max([[weighted_sum1,source1],[weighted_sum2,source2]])

		return maximum[1]

	def compare(self, source1, source2):
		'''Prints out a “classification report” that contains the lists of 
		similarity scores for source1 and source2 and a descriptive 
		statement for which source the TextModel self most likely originated 
		from '''
		print('Scores for source1: ', self.similarity_scores(source1))
		print('Scores for source2: ', self.similarity_scores(source2))

		print(self.name,'is more likely to have come from', \
			self.classify(source1,source2).name)

##
## Helper Methods:
##

def clean_text(txt):
	'''
	Returns a list of words consisting of the words in the
	output string in all lowercase letters and without punctuation;
	Input: a string
	'''
	text = txt

	if text == '':
		return []

	else:
		text_spaced = text.replace('-',' ')
		words = text_spaced.split(' ')
		words_list = list(filter(lambda x: len(x) > 0, words))

		exclude_list = list(map(lambda x: chr(x), list(range(32,65)) + \
			list(range(91,97)) + list(range(123,128))))

		for word in range(len(words_list)):
			for ch in exclude_list:
				words_list[word] = words_list[word].replace(ch,'').lower()

		return words_list


def stem(word):
	'''
	Returns the word stem of the input word;
	Input: a string
	'''
	if len(word) < 4:
		return word

	else:

		return_word = word

		if return_word[-1] == 's':
			if return_word[-3:] == 'ous':
				return_word = return_word[:-3]
			else:
				return_word = return_word[:-1]

		if return_word[-1] == 'y':
			if return_word[-2] == 'l':
				return_word = return_word[:-2]
			else:
				return_word = return_word[:-1] + 'i'

		if return_word[-1] == 'e':
			return_word = return_word[:-1]

		if return_word[-3:] == 'ing':
			return_word = return_word[:-3]

		if return_word[-2:] == 'er':
			return_word = return_word[:-2]

		if return_word[-2:] == 'ed':
			return_word = return_word[:-2]

		if return_word[:2] == 're':
			return_word = return_word[2:]

		if return_word[:2] == 'un':
			return_word = return_word[2:]

		if return_word[:3] == 'dis':
			return_word = return_word[3:]

		if return_word[:3] == 'non':
			return_word = return_word[3:]

		if return_word[:3] == 'pre':
			return_word = return_word[3:]

		if len(return_word) > 3:
			if return_word[-1] == return_word[-2]: 
				return_word = return_word[:-1]


		return return_word

def sentence_split(text):
	''' Method to split input text into a list of sentences '''
	text = text.replace('?','.')
	text = text.replace('!','.')

	return text.split('.')

def compare_dictionaries(d1, d2):
	''' Consumes 2 feature dictionaries d1 and d2.
		Computes and returns their log similarity score
		using the Naive Bayes scoring algorthm
	'''
	score = 0
	total = sum(d1.values())

	if total == 0 or d1 == {} or d2 == {}:
		pass
	else:
		for item in d2:
			if item in d1:
				score += log(d1[item] / total) * d2[item]
			else:
				score += log(0.5 / total) * d2[item]
	
	return score

def similarity_scores(self, other):
	'''Consumes another TextModel.
	   Computes and returns a list of log similarity scores measuring
	   the similarity of self and other, one score for each type of feature
	'''
	word_score = compare_dictionaries(other.words,self.words)
	length_score = compare_dictionaries(other.word_lengths,self.word_lengths)
	stem_score = compare_dictionaries(other.stems,self.stems)
	sentence_length_score = \
	compare_dictionaries(other.sentence_lengths,self.sentence_lengths)
	punctuation_score = \
	compare_dictionaries(other.punctuation,self.punctuation)
	stop_words_score = \
	compare_dictionaries(other.stop_words,self.stop_words)

	return [word_score,length_score,stem_score] + \
	[sentence_length_score,punctuation_score,stop_words_score]

def run_experiments():
	''' Test compare method with multiple sources '''
	# Simple texts
	source1 = TextModel('source1')
	source1.add_string('It is interesting that she is interested.')

	source2 = TextModel('source2')
	source2.add_string('I am very, very excited about this!')

	mystery = TextModel('mystery')
	mystery.add_string('Is he interested? No, but I am.')
	mystery.compare(source1, source2)

	# Family Guy and Spongebob tested with Big Bang Theory
	source1 = TextModel('Family Guy')
	source1.add_file('FamilyGuyScripts.txt')

	source2 = TextModel('Spongebob')
	source2.add_file('Spongebob.txt')

	new = TextModel('FamilyGuyE20') #test family guy episode
	new.add_file('FamilyGuyE20.txt')
	new.compare(source1,source2)

	new1 = TextModel('Big Bang Theory')
	new1.add_file('BBT.txt')
	new1.compare(source1,source2)

	# Crime and Punishment and Lord of the Rings tested with harry potter
	source1 = TextModel('Crime and Punishment')
	source1.add_file('CrimeAndPunishment.txt')

	source2 = TextModel('Lord of the Rings')
	source2.add_file('LordOfTheRings.txt')

	new = TextModel('CAPLastChapter') #test last chapter
	new.add_file('CAPLastChap.txt')
	new.compare(source1,source2)

	new1 = TextModel('Harry Potter')
	new1.add_file('HP.txt')
	new1.compare(source1,source2)

	# Saw and Titanic tested with mean girls
	source1 = TextModel('Saw')
	source1.add_file('Saw.txt')

	source2 = TextModel('Titanic')
	source2.add_file('Titanic.txt')

	new = TextModel('TitanicEnding') #test part of titanic
	new.add_file('TitanicEnding.txt')
	new.compare(source1,source2)

	new1 = TextModel('Mean Girls')
	new1.add_file('MeanGirls.txt')
	new1.compare(source1,source2)

	#Roald Dahl vs Poe
	source1 = TextModel('Roald Dahl')
	source1.add_file('RoaldDahl.txt')

	source2 = TextModel('Poe')
	source2.add_file('Poe.txt')

	new = TextModel('Poe Short Story') #test one short story from Poe
	new.add_file('PoeTellTaleHeart.txt')
	new.compare(source1,source2)

	new1 = TextModel('Dr. Seuss')
	new1.add_file('CatintheHat.txt')
	new1.compare(source1,source2)

run_experiments()

##
## Test Cases
##

def test_stem():
	'''
	Test cases for stem function
	'''
	assert stem('party') == 'parti'
	assert stem('parties') == 'parti'
	assert stem('love') == 'lov'
	assert stem('loving') == 'lov'
	assert stem('swimming') == 'swim'
	assert stem('uneducated') == 'educat'
	assert stem('programmer') == 'program'
	assert stem('hi') == 'hi', '2 letter case'
	assert stem('I') == 'I', 'one letter case'
	assert stem('') == '', 'blank'

test_stem()

def test_sentence_split():

	text1 = 'Hello'
	text2 = 'Hello? Hi everyone!'
	text3 = ''

	assert sentence_split(text1) == ['Hello']
	assert sentence_split(text2) == ['Hello', ' Hi everyone', '']
	assert sentence_split(text3) == ['']

test_sentence_split()

def test_clean_text():
	'''
	Test cases for clean_text function
	'''
	text = "This has LOTS of punctuation--let's clean this!"
	cleaned_text = ['this','has','lots','of','punctuation', \
	'lets','clean','this']
	assert clean_text(text) == cleaned_text, 'General case failed'
	assert clean_text('') == [], 'Empty string case failed'
	assert clean_text(' ') == [], 'Space string case failed'

	text2 = "tEst caSE!!!"
	cleaned_text2 = ['test', 'case']
	assert clean_text(text2) == cleaned_text2,'Capitalization, multiple punct'
	text3 = "1234@"
	assert clean_text(text3) == [''], 'symbols'

test_clean_text()


def test_TextModel___repr__():
	'''
	Test cases for TextModel  __repr__ method
	'''
	model = TextModel('A. Poor Righter')

	modelPrint = 'text model name: A. Poor Righter' + '\n' + \
	'  number of words: 0' + '\n' + \
	'  number of word lengths: 0' + '\n' + \
	'  number of stems: 0' + '\n' + \
	'  number of sentence lengths: 0' + '\n' + \
	'  number of punctuation marks: 0' + '\n' + \
	'  number of stop words: 0'

	assert str(model) == modelPrint, 'Empty failed'
	model.add_string("The partiers love the pizza party.")
	modelPrint = 'text model name: A. Poor Righter' + '\n' + \
	'  number of words: 5' + '\n' + \
	'  number of word lengths: 4' + '\n' + \
	'  number of stems: 4' + '\n' + \
	'  number of sentence lengths: 1' + '\n' + \
	'  number of punctuation marks: 1' + '\n' + \
	'  number of stop words: 1' 
	assert str(model) == modelPrint, 'General case failed'

test_TextModel___repr__()

def test_add_string():
	'''Test cases for add_string method
	'''
	model = TextModel('Sample')
	model.add_string('A sample sampling text? Yes.')
	assert model.words == {'a': 1, 'sample': 1, 'sampling': 1, 'text': 1, \
	'yes': 1}, 'general case words'
	assert model.word_lengths == {1: 1, 6: 1, 8: 1, 4: 1, 3: 1}, \
	'words_lengths different'
	assert model.stems == {'a': 1, 'sampl': 2, 'text': 1, 'yes': 1}, \
	'stems different'
	assert model.sentence_lengths == {4: 1, 1: 1}, \
	'sentence_lengths different'
	assert model.punctuation ==	{'?': 1, '.': 1}, 'punctuation different'
	assert model.stop_words == {'a': 1}, 'stop words different'

	model = TextModel('Sample2')
	model.add_string('NO?!')
	assert model.words == {'no': 1}, 'words different'
	assert model.word_lengths == {2: 1}, \
	'words_lengths different'
	assert model.stems == {'no': 1}, \
	'stems different'
	assert model.sentence_lengths == {1: 1}, \
	'sentence_lengths different'
	assert model.punctuation ==	{'?': 1, '!': 1}, 'punctuation different'
	assert model.stop_words == {'no':1}, 'stop words different'

test_add_string()

def test_add_file():
	'''Test add_file method'''
	#test blank case
	model = TextModel('Sample3')
	model.add_file('blank.txt')
	assert model.words == {}, 'blank test'
	#test file with no punctuation
	model = TextModel('Sample4')
	model.add_file('no_punct.txt'),'file with no punctuation'
	assert model.punctuation == {}
	assert model.words == {'a': 1,'b': 1,'c': 1,'ddd': 1}
	model = TextModel('Sample5')
	model.add_file('one_word.txt')
	assert model.sentence_lengths == {1:1}, 'general case'

test_add_file()

def test_save_read_model():
	''' Joint test cases for save_model and read_model '''
	#Test Case 1
	str1 = "aa bb cc dd !"
	m1 = TextModel('1')
	m1.add_string(str1)
	m1.save_model()

	m1_new = TextModel('1')
	m1_new.read_model()
	assert m1_new.words == m1.words, 'words different'
	assert m1_new.word_lengths == m1.word_lengths, 'words_lengths different'
	assert m1_new.stems == m1.stems, 'stems different'
	assert m1_new.sentence_lengths == m1.sentence_lengths, \
	'sentence_lengths different'
	assert m1_new.punctuation == m1.punctuation, 'punctuation different'
	assert m1_new.stop_words == m1.stop_words, 'stop words different'

	str1 = "" #test blank file
	m1 = TextModel('1')
	m1.add_string(str1)
	m1.save_model()

	m1_new = TextModel('1')
	m1_new.read_model()
	assert m1_new.words == m1.words, 'blank'
	assert m1_new.word_lengths == m1.word_lengths, 'blank'
	assert m1_new.stems == m1.stems, 'blank'
	assert m1_new.sentence_lengths == m1.sentence_lengths, 'blank'
	assert m1_new.punctuation == m1.punctuation, 'blank'
	assert m1_new.stop_words == m1.stop_words, 'blank'

test_save_read_model()

def test_classify():
	'''
	Test cases for classify method
	'''
	source1 = TextModel('source1')
	source1.add_string('This is a computer science course')

	source2 = TextModel('source2')
	source2.add_string('I also do CS')

	mystery = TextModel('mystery')
	mystery.add_string('I do CS.')
	assert mystery.classify(source1,source2).name == 'source2', \
	'general case'

	source1 = TextModel('source1')
	source1.add_string('I am Sarah')

	source2 = TextModel('source2')
	source2.add_string('I like to go swimming')

	mystery = TextModel('mystery')
	mystery.add_string('An apple')
	assert mystery.classify(source1,source2).name == 'source1', \
	'general case'

test_classify()

def test_compare_dictionaries():
	'''
	Test cases for compare_dictionaries function
	'''
	source1 = TextModel('source1')
	source1.add_string('It is interesting that she is interested.')

	source2 = TextModel('source2')
	source2.add_string('I am very, very excited about this!')

	mystery = TextModel('mystery')
	mystery.add_string('Is he interested? No, but I am.')

	a = compare_dictionaries(source1.words,mystery.words)
	b = compare_dictionaries(source2.words,mystery.words)
	c = compare_dictionaries(source2.punctuation,mystery.punctuation)

	assert a > -16.393959765627 and a < -16.393959765626, \
	'general case for words'
	assert b > -17.087106946187 and b < -17.087106946186, \
	'general case for words'
	assert c > -3.4657359027998 and c < -3.4657359027997, \
	'general case for punctuation'

	source1 = TextModel('source1')
	source1.add_string('This.')

	source2 = TextModel('source2')
	source2.add_string('Is a test!')

	mystery = TextModel('mystery')
	mystery.add_string('I do CS.')

	a = compare_dictionaries(source1.words,mystery.words)
	b = compare_dictionaries(source2.words,mystery.words)
	c = compare_dictionaries(source2.word_lengths,mystery.word_lengths)

	assert a > -2.0794415416799 and a < -2.0794415416798, \
	'general case for words'
	assert b > -5.375278407685 and b < -5.375278407684, \
	'general case for words'
	assert c > -3.295836866005 and c < -3.295836866004, \
	'general case for words'

test_compare_dictionaries()

def test_similarity_score():
	'''
	Test cases for similarity score function
	'''
	source1 = TextModel('source1')
	source1.add_string('It is interesting that she is interested.')

	source2 = TextModel('source2')
	source2.add_string('I am very, very excited about this!')

	mystery = TextModel('mystery')
	mystery.add_string('Is he interested? No, but I am.')
	
	a = sum(mystery.similarity_scores(source1))
	b = sum(mystery.similarity_scores(source2))

	assert a > -57.21664633906 and a < -57.21664633905, \
	'general case'
	assert b > -67.55705509841 and b < -67.55705509840, \
	'general case'

	source1 = TextModel('source1')
	source1.add_string('This.')

	source2 = TextModel('source2')
	source2.add_string('Is a test!')

	mystery = TextModel('mystery')
	mystery.add_string('I do CS.')

	c = sum(mystery.similarity_scores(source1))
	d = sum(mystery.similarity_scores(source2))

	assert c > -8.317766166720 and c < -8.317766166719, \
	'general case'
	assert d > -17.512129584173 and d < -17.512129584172, \
	'general case'

test_similarity_score()
