#!/usr/bin/env python3

def return_evens(num_list):
    evens = [n for n in num_list if n % 2 == 0]
    return evens
    

def make_exclamation(sentence_list):
    changed_sentences = [s + "!" for s in sentence_list ]
    return changed_sentences