from random import choice
import sys
import string

def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # Open file
    with open(file_path) as text_file:
        # Read entire file
        text = text_file.read()

    return text


def make_chains(text_string, n=3):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """
    chains = {} # Create empty dictionary

    words = text_string.split() # Split text into list of words
    i = 0
    for i in range(len(words)-(n)):

        word_key = tuple(words[i:i+n])
        chains[word_key] = chains.get((word_key), [])

        chains[word_key].append(words[i+n])

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = "" # Creates empty string

    # Find a random key(a tuple) from the chains dictionary, and store it in first_n_words
    while True:
        first_n_words = choice(chains.keys()) 

        if first_n_words[0][0].isupper():
            break
        else:
            continue
    # chains.get gives you a list of values for the first_n_words, 
    # and choice picks a random one, which we store in next_word
    next_word = choice(chains.get(first_n_words))
    # Concatenate both words in the first_n_words, and the next_word to the text string
    
    for item in first_n_words:
        text = text + " " + item

    text = text + " " + next_word

    while True:
        next_n_words = first_n_words[1:] + (next_word,)

        if chains.get(next_n_words) == None:
            break

            # CODE TO DO PUNCTUATION HERE
            if chains.get(next_n_words)[0][len(next_n_words)-1] in string.punctuation:
                break
            else: 
                continue
                
        else:
            first_n_words = next_n_words
            next_word = choice(chains.get(next_n_words))

            text = text + " " + next_word

    return text


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
