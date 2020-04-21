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


def all_tags_in_a_sentence(emission_dict, words):
    emission_of_list_of_words = {}
    temp_words = []
    for n in words:
        rregex = ""
        for a in n:
            rregex += "[" + a + "]"
        temp_words.append("^" + rregex + "[/]")
    for i in emission_dict:
        for j in temp_words:
            if re.match(j, i):
                emission_of_list_of_words[i] = emission_dict[i]
    all_tags = []
    for i in emission_of_list_of_words:
        temp = re.split("/", i)[1]
        if temp not in all_tags:
            all_tags.append(temp)
    return emission_of_list_of_words, all_tags


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


def emissions_probability(ep_emissions, words):
    temp_dict = ep_emissions
    for n in words:
        regex_maker = "^" + n + "[/]"
        for o in temp_dict:
            if re.match("[()]", n):
                1
            elif re.match(regex_maker, o):
                print(o, temp_dict[o])

def s_getter(number, tag_set):
    if number < 1:
        return ["*"]
    else:
        return tag_set

def tag_sequence_of_sentence(sentence_string):
    split = sentence_string.split()
    sequence = []
    for i in split:
        sequence.append(re.split("/", i)[1])
    return sequence

def create_translations(tri_sequence, transmissions):
    tri_transmissions = []
    for i in transmissions:
        tri_transmissions.append(i.split())
    tri_tags = tri_sequence
    denominator = 0
    for j in tri_transmissions:
        if tri_tags[0] == j[0] and tri_tags[1] == j[1]:
            match = j[0] + " " + j[1] + " " + j[2]
            denominator += transmissions[match]
    numerator = transmissions[tri_tags[0] + " " + tri_tags[1] + " " + tri_tags[2]]
    if denominator == 0:
        tri_tags.append(0)
    else:
        tri_tags.append(numerator / denominator)
    return(tri_tags)

def create_emissions(sequence, emissions):
    bi_emissions = []
    for i in emissions:
        bi_emissions.append(re.split("/", i))
    sequence = [re.split("/", sequence[0])[0], sequence[1]]
    # print(sequence)
    # pprint(emissions)
    denominator = 0
    match = ""
    for j in bi_emissions:
        if sequence[0] == j[0]:
            match = j[0] + "/" + j[1]
            # print(match)
            denominator += emissions[match]
        numerator = emissions[sequence[0] + "/" + sequence[1]]
    if(sequence[0]) == "*":
        return 1
    elif denominator == 0:
        return 0
    else:
        return numerator / denominator




def viterbi(sentence_string, v_transmissions, v_emissions):
    # viterbi algorithm takes one sentence at a time
    # pass in the sentence as a string WITH stars and STOP in the file

    # pi table 0=k_index 1=u 2=v 3=pi 4=bp
    pi_table = [[0], ["*"], ["*"], [""]]
    # words start from index 1

    sentence_in_list = sentence_string_to_list(sentence_string)
    all_words = all_words_in_a_sentence(sentence_in_list)
    unique_emissions, all_tags = all_tags_in_a_sentence(v_emissions, all_words)
    # pprint(unique_emissions)
    # print(all_tags)

    tags_in_order = tag_sequence_of_sentence(sentence_string)
    tri_sequence = ngrams(tags_in_order, 3)
    # print(tri_sequence)
    # pprint(v_transmissions)
    # # # print(create_translations(tri_sequence,v_transmissions))

    # pprint(v_emissions)
    # input()
    # pi table indexes
    #   0   1   2   3   4
    #   k   U   V   Pi  BP
    #   0   *   *   1   ""
    pi_table = [[0, "*", "*", 1, ""]]
    for k in range(1,len(sentence_string.split())):
        for u in s_getter(k-1, all_tags):
            for v in s_getter(k, all_tags):
                pi_max = -1
                bp_max = ""
                for w in s_getter(k - 2, all_tags):
                    value = 0;
                    pi_value = 0
                    for pi in pi_table:
                        if pi[0] == k - 1 and pi[1] == w and pi[2] == u:
                            pi_value = pi[3]
                    q = [w, u, v]
                    e = [sentence_string.split()[k], v]
                    # print(pi_value)
                    # print(q)
                    # print(e)
                    q = create_translations(q, v_transmissions)[3]
                    e = create_emissions(e, v_emissions)
                    max_value = pi_value * q * e
                    if max_value > pi_max:
                        pi_max = max_value
                        bp_max = w



    # print(sentence_in_list)
    # if sentence 37 long, go from 1 to 36
    return "doesn't completely work, read comment on submission"


# argv 0 program name, 1 training file, 2 test file

training_file = open(argv[1]).read()
train_file = open(argv[1])
test_file = open(argv[2])

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


# TODO change from one sentence to iterate through entire list
print(viterbi(test_file_sentences_formatted[1], transmissions_trigram_dictionary, emissions))



#### test files ####
