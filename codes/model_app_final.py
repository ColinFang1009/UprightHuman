from gensim.models import word2vec, Word2Vec 
import gensim
import numpy as np
from sklearn.decomposition import PCA
import pandas as pd

# for-loop to process bulk files
# for i in range(1994, 1996):
#     year = str(i)
year = "2003-2"
file_path = './{}.txt'.format(year)

sentences = word2vec.LineSentence(file_path)
    #train the model
model = word2vec.Word2Vec(sentences, hs=1,min_count=1,window=3,size=100)  

    # def dist(vec1, vec2):
    #     return sum((vec1-vec2)**2)
    # def cos_dist(vec1, vec2):
    #     return (np.dot(vec1, vec2)/np.linalg.norm(vec1)/np.linalg.norm(vec2))

    #Initialize name list, similarity list, vector list
s_list = np.array(["人民"])
simi_list = np.array([1])
vec_people = model.wv["人民"]
vec_list = np.array([model.wv["人民"]])
    # Find words with top 10 similarity, append respective properties to the arrays
for key in model.wv.similar_by_word('人民', topn = 30):
    word = key[0]
    similarity = key[1]
    s_list = np.concatenate((s_list, [word]), axis=0)
    simi_list = np.concatenate((simi_list, [similarity]), axis=0)
    vec = model.wv[word]
    vec_list = np.concatenate((vec_list,[vec]),axis=0)

    # PCA reduce the vectors to 2D
X_reduced = PCA(n_components=2).fit_transform(vec_list)   

    # Initialize xValue and yValue array.
x_value = np.array([])
y_value = np.array([])

    #Append values to the arrays
for element in X_reduced:
    x_value = np.concatenate((x_value, [element[0]]), axis=0)
    y_value = np.concatenate((y_value, [element[1]]), axis=0)

    # Use pandas to save the information in a .csv file
dict = {'name': s_list, 'similarity': simi_list, 'xValue': x_value, 'yValue': y_value}       
df = pd.DataFrame(dict)
    # saving the dataframe  
df.to_csv("{}.csv".format(year))  
