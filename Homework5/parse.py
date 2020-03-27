#!/usr/bin/env python3
""" tagging """
__author__ = "Nolan Shikanai"

from sys import argv
from collections import Counter
import re
from pprint import pprint


def ngrams(text, n):
    return [' '.join(text[i:i + n]) for i in range(len(text) - n + 1)]


def split_tags(tags_list):
    return_non_terminals = []
    for i in tags_list:
        a = re.split("/", i)
        return_non_terminals.append(a[1])
    return return_non_terminals


def split_words(words_list):
    return_non_terminals = []
    for i in words_list:
        a = re.split("/", i)
        return_non_terminals.append(a[0])
    return return_non_terminals

def test_corpus_new_line_cleanse(sentences_in_list):
    temp = []
    for n, i in enumerate(sentences_in_list):
        if i is not "\n":
            temp.append(i)
    return temp


def emissions_dict_matcher(word, emissions_dictionary):
    # takes the word you want, and the dictionary, returns the probability the word is that tag
    regex_match = "^" + word + "[/]"
    total = 0
    matching_emissions = []
    for i in emissions_dictionary:
        if re.findall(regex_match, i):
            total += emissions_dictionary[i]
            temp_list = [i, emissions_dictionary[i]]
            matching_emissions.append(temp_list)
    # print(total)
    # print(matching_emissions)
    for i in matching_emissions:
        i[1] = i[1] / total
    # print(matching_emissions)
    return matching_emissions


def sentence_formatting(list_of_sentences):
    temp = list_of_sentences
    # temp = remove_new_line_and_tabs(temp)
    temp = add_stop_to_end_of_sentence(list_of_sentences)
    temp = add_star_to_start_of_sentence(temp)
    temp = add_star_to_start_of_sentence(temp)
    return temp


def remove_new_line_and_tabs(list_of_sentences):
    temp = []
    for i in list_of_sentences:
        if i[0] == '\t' and i[-1] == '\n':
            i = i[1:-1]
        if i[-1] == '\n':
            i = i[:-1]
        if i[0] == '\t':
            i = i[1::]
        temp.append(i)
    return temp


def add_stop_to_end_of_sentence(list_of_sentences):
    temp = []
    for i in list_of_sentences:
        i = i + " STOP/STOP"
        temp.append(i)
    return temp


def add_star_to_start_of_sentence(list_of_sentences):
    temp = []
    for i in list_of_sentences:
        i = "*/* " + i
        temp.append(i)
    return temp


def transmissions(list_of_tags, given1, given2, trigrams_dict):
    transmission_probabilities = []
    running_total = 0
    for i in list_of_tags:
        dictionary_match = given1 + " " + given2 + " " + i
        transmission_probabilities.append([dictionary_match, trigrams_dict[dictionary_match]])
        running_total += int(trigrams_dict[dictionary_match])
    for n in transmission_probabilities:
        n[1] = int(n[1]) / running_total
    return transmission_probabilities


def all_tags_in_a_sentence(sentence_list):
    all_unique_tags = []
    # separating the words from the tags
    temp = []
    for i in sentence_list[1:]:
        temp.append(re.split("[/]", i)[1])
    for i in temp:
        if i not in all_unique_tags:
            all_unique_tags.append(i)
    return all_unique_tags

def all_words_in_a_sentence(sentence_list):
    all_unique_words = []
    # separating the words from the tags
    temp = []
    for i in sentence_list[1:]:
        temp.append(re.split("[/]", i)[0])
    for i in temp:
        if i not in all_unique_words:
            all_unique_words.append(i)
    return all_unique_words

def sentence_string_to_list(sentence):
    # starts from element 1
    sentence_list = [""]
    a = sentence.split()
    for i in a:
        sentence_list.append(i)

    # removing stars and STOP
    sentence_list.remove(sentence_list[1])
    sentence_list.remove(sentence_list[1])
    sentence_list.remove(sentence_list[-1])
    return sentence_list


def creating_all_emissions_dict(unique_tags_in_list, unique_words_in_list, emissions):
    # print(emissions_dict_matcher("left", emissions))
    the_dict = {}
    for n in unique_words_in_list:
        for a in unique_tags_in_list:
            unique_word_count = 0
            word_tag_combo = n + "/" + a
            if word_tag_combo in emissions:
                unique_word_count += int(emissions[word_tag_combo])
                the_dict[word_tag_combo] = int(emissions[word_tag_combo])
            else:
                the_dict[word_tag_combo] = 0
        if unique_word_count > 0:
            for k in the_dict:
                # print(the_dict[k])
                the_dict[k] = the_dict[k] / unique_word_count
                # print(unique_word_count)
                # print("###")
    return the_dict

def emissions_probability(ep_emissions):
    for i in emissions:
        if re.match("^in[/]", i):
            print(i)
            print(emissions[i])

def viterbi(sentence_string, v_transmissions, v_emissions):
    # viterbi algorithm takes one sentence at a time
    # pass in the sentence as a string WITH stars and STOP in the file

    # pi table 0=k_index 1=u 2=v 3=pi 4=bp
    pi_table = [[0], ["*"], ["*"], [""]]
    # words start from index 1

    sentence_in_list = sentence_string_to_list(sentence_string)
    all_tags = all_tags_in_a_sentence(sentence_in_list)
    all_words = all_words_in_a_sentence(sentence_in_list)
    emissions_dict = creating_all_emissions_dict(all_tags, all_words, v_emissions)
    #pprint(emissions_dict)
    # print(sentence_in_list)
    # if sentence 37 long, go from 1 to 36
    return -1


# argv 0 program name, 1 training file, 2 test file
# training_file = open(argv[1]).read()
# test_file = open(argv[2])
# TODO change this back to argv and not training text
training_file = open("ca_train.txt").read()
train_file = open("ca_train.txt")
test_file = open("ca_test.txt")

training_split = training_file.split()

#### training files ####
emissions = Counter(training_split)
non_terminals = Counter(split_tags(training_split))
unique_words = Counter(split_words(training_split))
two_non_terminals = Counter(ngrams(split_tags(training_split), 2))
three_non_terminals = Counter(ngrams(split_tags(training_split), 3))

### my verterbi ###

# each sentence is a list TEST FILE
test_file_sentences_formatted = sentence_formatting(test_corpus_new_line_cleanse(test_file.readlines()))
# each sentence is a list TRAIN FILE
train_file_sentences_formatted = sentence_formatting(test_corpus_new_line_cleanse(train_file.readlines()))

# creating the transmission_trigram_dictionary, tags in order for the transmissions
pre_ttd = []
for i in train_file_sentences_formatted:
    ttd = ngrams(split_tags(i.split()), 3)
    for j in ttd:
        pre_ttd.append(j)

transmissions_trigram_dictionary = Counter(pre_ttd)

# print(emissions_dict_matcher("left", emissions))

# print(transmissions(["nn", "jj", "pps"], "*", "*", transmissions_trigram_dictionary))
# pprint(test_file_sentences_formatted[1].split()[2:-1])


viterbi_emissions_probability = emissions_probability(emissions, unique_words)

# TODO change from one sentence to iterate through entire list
print(viterbi(test_file_sentences_formatted[1], transmissions_trigram_dictionary, emissions))
# TODO delete this pls
# print(viterbi("*/* */* ass/a bass/b ass/c ass/a ass/a bass/z STOP/STOP", transmissions_trigram_dictionary, emissions))



#### test files ####
