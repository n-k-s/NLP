import nltk
from nltk.corpus import stopwords
import regex
from nltk import pos_tag
from nltk import RegexpParser
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn
from nltk import word_tokenize, pos_tag
import random


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

###

print(sentence_similarity("Xerostomia", ""))
#
#
# text = word_tokenize(("""headache, fever, stomache ache, vomiting, nauseous, nausea, vomit""").lower())
#
# text = word_tokenize(("""I'm not feeling too well. I have a headache and chest pain""").lower())
# tokens_tag = pos_tag(text)
# print(tokens_tag)

###

symptoms = ["Fever", "Nausea", "Cough", "Light Headed", "Chills", "Tired"]

def dialogue_entrance():
    print("Welcome to the medical diagnosis tool, please list your symptoms")


def dialogue_confirmation():
    options = ["Okay", "Got it", "Ok"]
    print(options[random.randint(0, len(options) - 1)])

def dialogue_symptoms():
    print()


def dialogue_exit():
    print()


def symptom_checker(symptom_list, user_sentence):
    user_symptoms = []
    symptom_grams = ngrams(user_sentence.split(), 2)
    for i in symptom_grams:
        top_symptom = ["", 0]
        for j in symptom_list:
            sim = sentence_similarity(i,j)
            if sim > .5 and sim > top_symptom[1]:
                top_symptom[1] = sim
                top_symptom[0] = i
        if len(top_symptom[0]) != 0:
            user_symptoms.append(top_symptom[0])
    print(user_symptoms)
    print()


symptom_checker(symptoms, "I feel light headed")
