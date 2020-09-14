# Objective
This tool compares two texts and assigns them a similarity score. It can be used to compare two source texts to a comparison text to determine which source text is more likely to have shared an author with the sample text.

# Files
- [**model.py**](model.py) contains all code used in this project.
- [**sample-texts**](sample-texts) and [**test-files**](test-files) contain sample text files used in testing.

# Methodology
1. In this model, I decided to analyze texts using the following metrics:

	**words:** the number of times each word appears in the text

	**word length:** the number of times each word length appears in the 
		text; word length is computed by counting the number of 
		characters in the word, excluding anything that is not a letter

	**stems:** the number of times each word stem appears in the text

	  The following suffixes were removed from words:  
			   s, ous, y (becomes i), ly, e, ing, er, ed

	  The following prefixes were removed from words:  
			   re, un, dis, non, pre

	**sentence length:** the number of time each sentence length appears;
		the sentece length is computed by counting the number of words
		in the sentence; sentences are split in the model by '?', '!' and
		'.'

	**punctuation:** counts the number of times each non-letter character,
		excluding spaces, are used in the text

	**stopwords:** counts the number of times each stopword (commonly used
	words that search engines are programmed to ignore; they do not add
	meaning to the text) is used in the text. 

	The stopwords used in this model (excluding non-letter
	characters) are:  
			(ourselves, hers, between, yourself, but, again, there, about,
			once, during, out, very, having, with, they, own, an, be,
			some, for, do, its, yours, such, into, of, most, itself,
			other, off, is, am, or, who, as, from, him, each, the,
			themselves, until, below, are, we, these, your, his, through,
			dont, nor, me, were, her, more, himself, this, down, should,
			our, their, while, above, both, up, to, ours, had, she, all,
			no, when, at, any, before, them, same, and, been, have, in,
			will, on, does, yourselves, then, that, because, what, over,
			why, so, can, did, not, now, under, he, you, herself, has,
			just, where, too, only, myself, which, those, i, after, few,
			whom, being, if, theirs, my, against, a, by, doing, it, how,
			further, was, here, than)
      
2. Each text is represented by a TextModel object, which is a collection of dictionaries that define the above attributes.

3. A Naive Bayes scoring algorithm is used to calculate the likelihood of the two texts belonging to the same author. A score is computed for each of the text attributes listed above, and weights were assigned to the score for each attribute:
    * The *compare_dictionaries* method (line 357) calculates the Naive Bayes score for each text attribute.
    * The *classify* method (line 234) outlines the weights assigned to each text attribute.
    
        * The words and sentence lengths used in a text are common metrics used to determine the text's source, as these are often fairly unique to authors. For this reason, I gave them a high weight. Punctuation is often nearly irrelevant for script-like works, so I gave this a lower weight. Many stop words are often unavoidable when writing, so I decided to give this a lower weight as well. The weights for word length and stems were determined after trial and error with different texts.
        
The final resulting weighted score is referred to as the similarity score.

4. Using the *compare* method (line 251), two TextModel objects (source texts) can be compared to the original TextModel object (comparison text) to determine which of the source texts is most similar to the comparison text. This is done by comparing similarity scores.
    * *run_experiments* (line 394) contains several tests of this model
    
# Results
**Experiment 1:**
	
source 1: 'It is interesting that she is interested.'  
source 2: 'I am very, very excited about this!'

comparison text: 'Is he interested? No, but I am.'

This is included to easily look at the entire text to ensure the score list in the analysis made sense. 

Results:

The model determined that the comparison text was more similar to source 1 than to source 2.

**Experiment 2:**

source 1: Family Guy Season 15 Scripts (episodes 1-19)  
source 2: Spongebob Season 5 Scripts

comparison text 1: Family Guy Season 15 Episode 20 Script  
comparison text 2: Big Bang Theory (one random episode) Script

These sources were chosen in order to test the model on television show scripts. I chose to compare the final episode of the season of Family Guy I used in the source (which is not included in the source) against both sources to ensure that the model would determine that it is more similar to Family Guy than to Spongebob. I also compared a random episode of Big Bang Theory to these sources, as Big Bang Theory is an example of a television show that doesn't have an obvious relation to either of the sources.

Results:

The model determined that the Family Guy Season 15 Episode 20 
Script is more similar to the Family Guy Season 15 Scripts than 
to the Spongebob Season 5 Scripts. The random Big Bang Theory 
episode script is more similar to the Family Guy Scripts than to 
the Spongebob Scripts.

**Experiment 3:**
	
source 1: Crime and Punishment (excluding final chapter)  
source 2: Lord of the Rings (The Fellowship of the Ring)

comparison text 1: Final Chapter of Crime and Punishment  
comparison text 2: Harry Potter and the Sorcerer's Stone (First Chapter)

I chose these sources in order to test our model on novels. I chose
to compare the final chapter of Crime and Punishment (not included
in source 1) against the sources to ensure that the model would
determine that it is more similar to Crime and Punishment than to
Lord of the Rings. I also compared the first chapter of the Harry
Potter Series against these two sources, as it is another example of
a novel that is unrelated (by author) to the other sources. 

Results:

Logically, the model determined that the final chapter of Crime  
and Punishment is more similar to the rest of Crime and Punishment 
than to Lord of the Rings. The model determinded that the first 
chapter of Harry Potter is more similar to Crime and Punishment
than it is to Lord of the Rings, which I found surprising and
a possible weakness to the model.

**Experiment 4:**

source 1: Saw Episode 1 Script  
source 2: Titanic Script

comparison text 1: Titanic Final Scene Script  
comparison text 2: Mean Girls Script

I chose these sources in order to test our model on movies. I chose
to compare the final scene of Titanic (not included
in source 1) against the sources to ensure that the model would
determine that it is more similar to the rest of Titanic than to
Saw Episode 1. I also compared the script of the movie Mean Girls
against these two sources, as it is another example of a movie that
is unrelated by producer and genre to the other sources. 

Results:

The model determined that the final scene of Titanic is more
similar to the rest of the Titanic movie script than to the Saw
Episode 1 script. The model determinded that the script of Mean
Girls is more similar to the script of Titanic than to that of
Saw Episode 1.

**Experiment 5:**

source 1: Roald Dahl (3 short stories)  
source 2: Edgar Allen Poe (4 short stories)

comparison text 1: Tell-Tale Heart (by Edgar Allen Poe); not included in source text 2  
comparison text 2: The Cat in the Hat (Dr. Seuss)

I chose these sources in order to test our model on short stories. 
I chose to compare Tell-Tale Heart by Poe to the sources (which do
not include this story) to ensure that the model would determine that
it is more similar to other stories by Poe than to stories by Roald
Dahl. I also compared The Cat in the Hat by Dr. Seuss to the sources
as it is another example of a short story of an entirely different
genre.

Results:

The model determined that Tell-Tale Heart by Edgar Allen Poe is
more similar to Poe's other short stories than to short stories
by Roald Dahl. The model also determined that The Cat in the Hat
by Dr. Seuss is more similar to Roald Dahl's works than to Poe's
works. 

# Takeaways

For all of the experiments we performed, I had a comparison text that
was taken from the same source as one of the source texts, and the
model always correctly determined the correct source text for this
comparison text. In this sense, the model works well. There are, however,
some aspects of this comparison approach that may lead to some
inaccuracies in the results. For example, the heaviest weight is on
the word score, but the word score would naturally be much lower when
comparing works of different genres, even if they come from the same
author. For this reason, the model may not work as well on novels or
movies as it would on collections of short stories or poetry, where there
are multiple genres/subjects in each collection. This, however, could be
improved by adjusting the similarity score weights depending on the
types of works we are comparing. The model could also be improved by
adding more complex text analysis features, such as
sentiment analysis, which would be more accurate in differentiating
between authors than the basic tools utilized by this model.
