import json
from nltk_utils import tokenize, stem, bag_of_words
import numpy as np

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

with open('intents.json', 'r') as f:
    intents = json.load(f)
    
all_words = []
tags = []
xy = []

for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        tokenized_patterns = tokenize(pattern) 
        all_words.extend(tokenized_patterns)    #The append() function adds the full input to the list as a single item. extend() adds each item to the list independently after iterating through each one in the input.
        xy.append((tokenized_patterns, tag))
 
# print(tags)
# print(all_words)
# print(xy)
       
exclude_words = ['?', ',', '.', '!']

all_words = [stem(word) for word in all_words if word not in exclude_words]

all_words = sorted(set(all_words))
tags = sorted(set(tags))

x_train = []
y_train = []

for (pattern, tag) in xy:
    bag = bag_of_words(pattern, all_words)
    x_train.append(bag)
    
    label = tags.index(tag)
    y_train.append(label) # crossentropy loss
    
x_train = np.array(x_train)
y_train = np.array(y_train)

class ChatDataset(Dataset):
    def __init__(self):
        self.n_samples = len(x_train)
        self.x_data = x_train
        self.y_data = y_train
        
    #dataset[index]
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]
    
    def __len__(self):
        return self.n_samples
    
# Hyperparameters
batch_size = 8

dataset = ChatDataset()
train_loader = DataLoader(dataset = dataset, batch_size = batch_size, shuffle = True, num_workers = 2)
        