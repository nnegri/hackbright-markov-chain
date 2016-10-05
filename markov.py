from random import choice

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

    print chains
    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = "" # Creates empty string

    # Find a random key(a tuple) from the chains dictionary, and store it in first_key
    first_key = choice(chains.keys()) 
    # chains.get gives you a list of values for the first_key, 
    # and choice picks a random one, which we store in first_value
    first_value = choice(chains.get(first_key))
    # Concatenate both words in the first_key, and the first_value to the text string
    text = first_key[0] +  " " +  first_key[1] + " " + first_value
    
    # Loop until a condition breaks it
    #new_key = (first_key[1], first_value)

    while True:
        new_key = (first_key[1], first_value)
        print new_key
        print chains.get(new_key)

        if chains.get(new_key) == None:
            break
        else:
            new_value = choice(chains.get(new_key))
            text = text + " " + new_value
            
            first_key = (first_value, new_value)

        # tokens = text.rstrip().split()
        # text_key = (tokens[-2], tokens[-1])

        # text_value = choice(chains.get(text_key))
        # text = text + " " + text_value

        # if chains.get(text_key) == []:
        #     break 

        #break


    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
