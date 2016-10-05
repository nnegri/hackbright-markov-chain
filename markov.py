from random import choice
import sys

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


def make_chains(text_string):
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
    for i in range(len(words)-2): # Loop through all words, stopping at second to last
        # Each key is a tuple of the word at index i, and the word directly following
        # chains.get returns the value of that tuple; 
        # it creates an empty list of nothing is there already
        chains[words[i], words[i+1]] = chains.get((words[i], words[i+1]), [])
        # If there is already a list there, 
        # it will append the word following the word at index 1 in the tuple
        chains[words[i], words[i+1]].append(words[i+2])

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = "" # Creates empty string

    # Find a random key(a tuple) from the chains dictionary, and store it in first_two_words
    first_two_words = choice(chains.keys()) 
    # chains.get gives you a list of values for the first_two_words, 
    # and choice picks a random one, which we store in next_word
    next_word = choice(chains.get(first_two_words))
    # Concatenate both words in the first_two_words, and the next_word to the text string
    
    first_word = first_two_words[0]
    second_word = first_two_words[1]

    text = first_word + " " + second_word + " " + next_word

    while True:
        next_two_words = (second_word, next_word)

        if chains.get(next_two_words) == None:
            break
        else:
            next_next_word = choice(chains.get(next_two_words))
            text = text + " " + next_next_word

            second_word = next_word
            next_word = next_next_word


    return text


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
