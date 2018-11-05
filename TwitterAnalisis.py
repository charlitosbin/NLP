# %%

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from nltk.tokenize import word_tokenize, sent_tokenize

pd.set_option('display.max_column', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_seq_items', None)
pd.set_option('display.max_colwidth', 10)
pd.set_option('expand_frame_repr', True)

df = pd.read_csv("/Users/developer/Desktop/debate_2018_cdmexico_muestra.csv")
df.shape
row = df.head(10)['Text']
count = 0

amloWords = ["peje", "amlo", "andres", "manuel", "lopez", "obrador","morena"]
broncoWords = ["bronco", "jaime rodriguez"]
meadeWords = ["meade", "antonio","meade", "pri"]
anayaWords = ["anaya", "ricardo", "pan"]

amloTweets = []
broncoTweets = []
meadeTweets = []
anayaTweets = []

for x in row:
    print(str(count) + ".- " + str(word_tokenize(row[count])))
    if any(word in row[count].lower() for word in amloWords):
        amloTweets.append(row[count])
    if any(word in row[count].lower() for word in broncoWords):
        broncoTweets.append(row[count])
    if any(word in row[count].lower() for word in meadeWords):
        meadeTweets.append(row[count])
    if any(word in row[count].lower() for word in anayaWords):
        anayaTweets.append(row[count])
    count += 1
