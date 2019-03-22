# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 14:08:11 2019

@author: Robothormones
"""

import pandas as pd
import string
from nltk.corpus import words
import csv
import random


def play_cowsnbulls():
    ##### Starts the Game####
    ### Now takes a number as input - which determines the size of the word###
    word_len = int(input("How many letter words do you want to play with? (Suggested - N=4) :\n"))
    ## Check if the word should be auto generated
    auto = str(input("Would you like to enter a challenge-word of your own? (Y/N):\n"))
    if str.upper(auto) == "N" or str.upper(auto) == "NO":
        auto = True
    else:
        auto = False
    # Begin by identifying a challenge word    
    challenge_word = create_challenge(word_len,auto)
    # to test if a challenge word is created, print the challenge word. 
#    print(challenge_word)
    
    # create a list called "history" which stores:
    # All previous words
    # Number of cows & Number of bulls from each word
    
    # Initiatte a History/Record of all attempts & their results
    history = []
    
    #Iterate attempts till the result is n bulls i.e it is complete. 
    # it is incomplete in the begining
    complete = False
    while complete is False:
        
        # Print the history showing all the words attempted & results
        summarize(history)
        # Request an attempt - 
        attempt = attempt_word(history, word_len,)
        # Test if the attempt_word function is working as expected
#        print(attempt)
        result = compare_words(attempt, challenge_word)
#        print("The Word [", result[0], "] has",result[1], "bulls and", result[2],"Cows")
        history = history + [result]
        
        if result[1]==word_len:
            complete = True
            print("\n"*10,"Congrats - you have completed the challenge.")
            print("The correct answer is", result[0])
            again = str(input("Would you like to go again? Y/N : "))
            if str.upper(again) == "Y":
                play_cowsnbulls()
            else:
                return()

def read_word_list(word_len):
    file_name = "word_list_"+str(word_len)+"_letters.csv"
    #### Load four_letter_word_list.csv ####
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        for i in reader:
            verified_word_list= i
    f.close()
    return(verified_word_list)
        
        
def create_challenge(word_len, auto=False):
    ### Input or auto-select a N letter word as a challenge###
    # if auto = False, ask for input
    if auto == False:
        challenge_word = str(input("Enter a {} letter word:".format(word_len)))
        if verify_word(challenge_word,word_len, verbose=True):
            #print 100 blank lines to clear the screen. Then indicate the game has begun.
            print("\n"*100)
            print("You have entered a good challenge. May the games begin!")    
        else:
            challenge_word=create_challenge(word_len, auto)
    else:
    # if auto = True, pick a word from the the word-list already saved.csv
        verified_word_list = read_word_list(word_len)
        challenge_word = random.choice(verified_word_list)
        print("I have identified a good challenge for you. May the games begin!")    
    
    return(challenge_word)
        
def verify_word(word, word_len, verbose = True):
    #### Test if the word entered is a valid challenge or attempt for the game ####
    
    ## Test: 
    # list = ["lion","pear","fool","asdfg","asd"]
    ## expect: 
    # [True, True, False, False, False]
        # Check if each character is a letter
    acceptable = True
    for i in word:
        if i not in string.ascii_letters:
            print("The word is not acceptable: Try again")
            return(False)
            # print("One of the characters is not a letter.")
            # return(False)
        else:
            word = str.lower(word)
    
    # check if there are only n letters
    if len(word)>word_len:
        # print("The word has more than n letters. Unacceptable!")
        # return(False)
        print("The word is not acceptable: Try again")
        return(False)
    elif len(word)<word_len:
        # print("The word has less than 4 letters. Unacceptable!")
        # return(False)
        print("The word is not acceptable: Try again")
        return(False)
    # check if there are repeating letters:
    if len(set(word))<word_len:
        # print("The word has repeating letters. Unacceptable!")
        # return(False)
        print("The word is not acceptable: Try again")
        return(False)
    # check if the word is in the dictionary
    verified_word_list = read_word_list(word_len)
    if word not in verified_word_list:
        print("The word is not acceptable: Try again")
        return(False)
    
            
    return(acceptable)
    

def compare_words(word, challenge_word):
    # cows - letter in wrong position
    # bulls - letter in correct position
    cows = 0
    bulls = 0
    
    for index,letter in enumerate(word):
        if letter in challenge_word:
            if challenge_word.index(letter)==index:
                bulls+=1
            else:
                cows+=1
    
    return([word,bulls,cows])
    
def attempt_word(history,word_len):
    
    attempt_no = len(history) + 1 
    print("\nEnter attempt word No.",attempt_no)
    attempt = str(input())
    if verify_word(attempt,word_len,verbose=True):
        print("Attempt Accepted. Comparing")
    else:
        print("Attempt Not Accepted. Try Again")
        attempt=attempt_word(history, word_len)
    return(attempt)
        


def summarize(history):
    # Test_History = [["lion",1,0],["pear",2,1],["fear",2,1],["crie",2,1],["zynt",2,1]]
    
#    print("You have not completed the challenge.\n Here is the history of your attempts")
    hist = pd.DataFrame(history, columns = ['attempted word','bulls','cows'])
    hist.index = hist.index+1
    print("***************************************************")
    print("*************** History of Attempts ***************")
    print("***************************************************")
    print(hist)
    
def make_word_list(word_len):
    #### Function to create a word-list from nltk.words ####
    #### to be used only once - but made into function in case i want to change up something later ####
    
    word_list = words.words()
    # four_letter_words = []

    verified_word_list= []
    for i in word_list:
        if len(i)==word_len:
            if verify_word(i,word_len,verbose=False):
                ### only retain verified words - to reduce the size of the file, and the search ###
                verified_word_list.append(str.lower(i))

            # four_letter_words.append(i)
            
    # for i in four_letter_words:
        # if verify_word(i,verbose=False):
        #     ### only retain verified words - to reduce the size of the file, and the search ###
        #     verified_4_letter_words.append(i)
    file_name = "word_list_"+str(word_len)+"_letters.csv"
    with open(file_name, 'w', newline="") as file:
        file_writer = csv.writer(file)
        file_writer.writerow(verified_word_list)
    print(verified_word_list)
    return()
    

    
play_cowsnbulls()
