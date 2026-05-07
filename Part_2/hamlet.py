# -*- coding: utf-8 -*-
"""
Tutorial file for Python for bioinformatics courses.
"""
import os.path


from word_tools import word_counts


def count_in_file(input_file, output_file):
    with open(input_file) as f:
        text = f.read()
        
    counts = word_counts(text)
    
    with open(output_file, 'w') as f:
        for wc in counts:
            f.write('%s : %d\n' % wc)
            
    return len(counts)


if __name__ == "__main__":
    input_file = './data/hamlet.txt'
    output_file = './data/hamlet_word_counts.txt'
        
    if os.path.exists(input_file):
        print("Loading", input_file)
        n = count_in_file(input_file, output_file)
        print(f'Found {n} distinct words in the provided part of "Hamlet".' % n)
    else:
        print("File not found:", input_file)
