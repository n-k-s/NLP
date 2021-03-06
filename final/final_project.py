#!/usr/bin/env python3
""" NLP Final Project """
__author__="Nolan Shikanai"
import csv
from nltk.corpus import wordnet as wn
from nltk import word_tokenize, pos_tag
import random

import time
import re


def dialogue_entrance():
    print("Welcome to the symptom diagnosis tool")
    time.sleep(.75)
    print("This tool is meant to help you get a general idea of what you may have")
    time.sleep(.75)
    print("This is not a replacement for a doctor or medical advice")
    time.sleep(.75)
    print("this has been made for academic purposes")
    time.sleep(.75)
    print()
    print("loading. . .")



dialogue_entrance()


def penn_to_wn(tag):
    if tag.startswith('N'):
        return 'n'
    if tag.startswith('V'):
        return 'v'
    if tag.startswith('J'):
        return 'a'
    if tag.startswith('R'):
        return 'r'
    return None


def tagged_to_synset(word, tag):
    wn_tag = penn_to_wn(tag)
    if wn_tag is None:
        return None

    try:
        return wn.synsets(word, wn_tag)[0]
    except:
        return None


def sentence_similarity(sentence1, sentence2):
    # Tokenize and tag
    sentence1 = pos_tag(word_tokenize(sentence1))
    sentence2 = pos_tag(word_tokenize(sentence2))

    # Get the synsets for the tagged words
    synsets1 = [tagged_to_synset(*tagged_word) for tagged_word in sentence1]
    synsets2 = [tagged_to_synset(*tagged_word) for tagged_word in sentence2]

    # Filter out the Nones
    synsets1 = [ss for ss in synsets1 if ss]
    synsets2 = [ss for ss in synsets2 if ss]

    score, count = 0.0, 0

    arr_similarity_score = []

    for syn1 in synsets1:
        best = 0.0
        for syn2 in synsets2:
            simi_score = syn1.wup_similarity(syn2)
            if simi_score is not None:
                arr_similarity_score.append(simi_score)
                best = max(arr_similarity_score)
                score += best
                count += 1
    if count == 0:
        score = 0
    else:
        score /= count
    return score


def ngrams(text, n):
    return [' '.join(text[i:i + n]) for i in range(len(text) - n + 1)]


diseases_and_symptoms = {}
all_symptoms = {}
with open('dataset.csv', 'rt')as f:
    data = csv.reader(f)
    for i in data:
        if i[0] not in diseases_and_symptoms:
            diseases_and_symptoms[i[0]] = []
        diseases_and_symptoms[i[0]].append(i[1])

with open('symptoms.csv', 'rt')as f:
    data = csv.reader(f)
    for i in data:
        if i[2] == "symptom":
            all_symptoms[i[0]] = i[1]

###

# print(sentence_similarity("Xerostomia", ""))
#
#


# text = word_tokenize(("""headache, fever, stomache ache, vomiting, nauseous, nausea, vomit""").lower())
#
# text = word_tokenize(("""I'm not feeling too well. I have a headache and chest pain""").lower())
# tokens_tag = pos_tag(text)
# print(tokens_tag)

###

symptoms = ["Fever", "Cough", "Light Headed", "Chills", "Tired"]





def list_symptoms():
    print("please list your symptoms separated by commas")
    print("i.e.")
    print("I have a headache, my throat is sore, and a fever")
    return input()


def dialogue_confirmation():
    options = ["Okay", "Got it", "Ok"]
    print(options[random.randint(0, len(options) - 1)])


def dialogue_symptoms():
    print()


def dialogue_exit():
    print()


def symptom_checker(symptom_dict, user_sentence):
    user_symptoms = []
    symptom_grams = ngrams(user_sentence.split(), 2)
    symptom_grams += user_sentence.split()
    # print(symptom_grams)
    for i in symptom_grams:
        top_symptom = ["", 0]
        for j in symptom_dict:
            sim = sentence_similarity(i, j)
            # print(i + " - COMPARE - " + j + " " + str(sentence_similarity(i,j)))
            # CHANGE NUMBER FOR HIGHER THRESHHOLD
            if sim > .8:
                top_symptom[1] = sim
                top_symptom[0] = j
        if len(top_symptom[0]) != 0:
            user_symptoms.append(top_symptom[0])
    print(user_symptoms)

def symptom_checker_revised(user_list):
    likely = []
    for i in user_list:
        if i in all_symptoms:
            temp = [1.0, i]
            likely.append(temp)
            user_list.remove(i)
    for i in user_list:
        symptom = [0.0, ""]
        for j in all_symptoms:
            value = sentence_similarity(i,j)
            if value > symptom[0]:
                symptom[0] = value
                symptom[1] = j
        likely.append(symptom)
    return likely

def disease_finder(likely_symptoms_lst):
    # Name of disease, score
    most_likely = ["", 0.0]
    # print(likely_symptoms_lst)
    for i in diseases_and_symptoms:
        disease_symptoms = diseases_and_symptoms[i]
        score = 0.0
        matching = 0.0
        zz_top = []
        for x in likely_symptoms_lst:
            zz_top.append(x[1])
        for j in zz_top:
            # print(j)
            # print(disease_symptoms)
            if j in disease_symptoms:
                score += 2.0
                matching += 1
            # else:
            #     score -= 1.0
        matching = matching / len(disease_symptoms)
        score = score * matching
        if score > most_likely[1]:
            most_likely[0] = i
            most_likely[1] = score
        # print(score)
        # print(i)
        # time.sleep(2)
    return most_likely




# for i in all_symptoms:
#     print(str(sentence_similarity(i, "back pain")) + " SYMPTOM: " + i)


cleaningRegex = "[,]|and|[ ]a |^my[ ]|^I |[ ]my[ ]|[ ]I[ ]|have "
#
# symptom_checker(all_symptoms, "my head hurts")
#
# print(sentence_similarity("headache", "bleeding"))


a = list_symptoms()
a = re.sub(" have "," ", a)
a = re.sub(" a "," ", a)
b = re.split(cleaningRegex, a)
a = []
for i in b:
    if len(i) > 0 and i != " ":
        a.append(i)



# print(a)
likely_symptoms = symptom_checker_revised(a)
# print(likely_symptoms)
likely_disease = disease_finder(likely_symptoms)
print("Most likely diagnosis: " + likely_disease[0])