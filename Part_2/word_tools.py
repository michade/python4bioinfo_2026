#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Short module description
"""

def make_words_list(text, ignore):
    """Turn 'text' into a list of words, stripping characters in 'ignore'"""
    return [w.lower().strip(ignore) for w in text.split()]

def word_counts(text, ignore="?!.,;"):
    """
    Obtain word counts in a given string, ingoring certain characters.
    Words are separated by whitespace.
    
    Args:
        text - string to count words in.
        ignore - the characters to remove from beginnings/endings of words.
    Returns:
        List of tuples: (word, number_of_occurences)
        
    """
    words = make_words_list(text, ignore)
    # the method below is quite ineffective, but will do for now...
    word_counts = [
        (w, words.count(w))
        for w in set(words)
    ] 
    return word_counts