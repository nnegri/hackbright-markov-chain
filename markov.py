from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    with open(file_path) as text_file:
        text = text_file.read()
        #print text
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
    chains = {}

    words = text_string.split()
    i = 0
    for i in range(len(words)-2):
        chains[words[i], words[i+1]] = chains.get((words[i], words[i+1]), [])
        chains[words[i], words[i+1]].append(words[i+2])

    #print chains
    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    first_key = choice(chains.keys()) 
    first_value = choice(chains.get(first_key))
    text = first_key[0] +  " " +  first_key[1] + " " + first_value
    #print text

    new_key = (first_key[1], first_value)
    #print new_key
    for key in chains:
    while True:

        new_value = choice(chains.get(new_key))
        text = text + " " + new_value
        new_key = 
        print text


    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
