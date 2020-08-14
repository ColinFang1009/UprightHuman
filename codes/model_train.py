# import modules & set up logging
import logging
import os
from gensim.models import word2vec
import gensim.models
from gensim.test.utils import common_texts, get_tmpfile

#set config
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# Read the processed file
input = './demo.txt'
sentences = word2vec.LineSentence(input) 
# Train the model and name it sample.model
path = get_tmpfile("sample.model")

model = word2vec.Word2Vec(sentences, hs=1,min_count=1,window=3,size=100)  
# model = gensim.models.Word2Vec(sentences, size=100, window=5, min_count=1) 
# Another way to train the model
model.save("sample.model")