#### Name : Syed Khalid Ahmed
#### Marticulation number : 276970

#!/usr/bin/env python

import pickle
from pickle import load
import nltk

if __name__ == "__main__":

    file = open('tagged_data.pkl','rb')     # Open the file containing the POS tagger

    POS_tagger = pickle.load(file)          # Load the tagger object using pickle

    ## Load the saved NER classifier object
    ## This file was generated by the nltk-trainer python script which
    ## generates a Naive-Bayes trained classifier
    NER_classifier = nltk.data.load(('conll2000_NaiveBayes.pickle'))    

    string = "Germany is a very beautiful country".split()

    ## Tag the words using the previously made tagger
    tagged_data = POS_tagger.tag(string)

    ## Find the named entities using the NER classifier and the tagger
    output = NER_classifier.parse(tagged_data)

    ## Print the output
    print(output)