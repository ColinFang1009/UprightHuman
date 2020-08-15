from gensim.test.utils import common_texts, get_tmpfile
import gensim.models
from gensim.models import word2vec, Word2Vec 
import gensim
import numpy as np
from sklearn.decomposition import PCA

#l Load the pre-trained model
model = gensim.models.Word2Vec.load("./word2vec48.model")

# Ways to use the model
#输入与“人民”相近的n个词
def dist(vec1, vec2):
    return sum((vec1-vec2)**2)
def cos_dist(vec1, vec2):
    return (np.dot(vec1, vec2)/np.linalg.norm(vec1)/np.linalg.norm(vec2))

s_list = []
vec_list = []
for key in model.wv.similar_by_word('人民', topn = 10):
    s_list.append(key)
    vec = model.wv[key]
    vec_list.append(vec)
    print(key)


print(model.wv[s_list])
x_reduced = PCA(n_components=2).fit_transform(model.wv[s1])
print(x_reduced)

vector_1 = model.wv[s_list[0]]
vector_2 = model.wv[s_list[1]]

print("Similarity between" + s1 + "and" + s2 + " : "+ str(model.wv.similarity(s1, s2)))
print("Cos Distance (sefdef) is " + " : " +  str(cos_dist(vector_1, vector_2)))
print("Distance sefdef is " + ":" + str(dist(vector_1, vector_2)))
print("Distance is : " + str(model.wv.distance(s1, s2)))
print("Similar by vector" + str(model.wv.similar_by_vector(vector_1)))
# print(model.wv.similar_by_vector(vector_1-vector_2))