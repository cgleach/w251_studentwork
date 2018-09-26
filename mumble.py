from subprocess import call
import numpy as np
import pandas as pd
import os
import random
import sys

def mumble_once(word):
    first_letter = word[0]
    os.system("zgrep -i -w '^{word}' /gpfs/gpfsfpo/preprocess_2/words_{first_letter}.csv.zip > \
              /gpfs/gpfsfpo/test.csv".format(first_letter=first_letter,word=word))
    final_df = pd.read_csv("/gpfs/gpfsfpo/test.csv",sep=" ",names=['ngram','second_word','quantity'])

    final_df['ngram'] = final_df['ngram'].str.lower()
    final_df['second_word'] = final_df['second_word'].str.lower()
    final_df = final_df.groupby(['ngram','second_word']).agg({'quantity':'sum'}).reset_index()
    final_df['quantity'] = final_df['quantity'].astype(int)

    if final_df.shape[0]==0:
        print("No words match, exiting")
        return False
    else:
        mumbler = dict(zip(final_df['second_word'].tolist(),final_df['quantity'].tolist()))
        new_word = pick_new_word(mumbler)
    return new_word

 
def pick_new_word(options):
    total=sum(options.values())
    selection = random.randint(1,total)
    counter = 0
    for k,v in options.items():
        if counter + v >= selection:
            return k
        counter += v
    return False

def mumble_consistently(word,length):
    final_list = [word]
    counter = 0
    while counter < length:
        word = mumble_once(word)
	if not word:
	    break
	else:
	    final_list.append(word)
            counter += 1
    print("Are you ready to mumble!!!!")
    print(final_list)
    os.system("rm /gpfs/gpfsfpo/test.csv")
    return final_list


def run():
    selections_satisfied = False

    while not selections_satisfied:
        try:
	    choice =str(input("What word do you want to use?"))
	    choice = choice.lower()
	    length = int(input("How long should the mumbler go?"))
	    if ((choice.isalpha()) and (isinstance(length,int))):
	        selections_satisfied = True
        except:
            print("Inputs aren't valid, try again")

    mumble_list = mumble_consistently(choice,length)
    return

run()
