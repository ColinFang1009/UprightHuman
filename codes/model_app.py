from gensim.test.utils import common_texts, get_tmpfile
import gensim.models
from gensim.models import word2vec, Word2Vec 
import gensim

#l Load the pre-trained model
model = gensim.models.Word2Vec.load("./word2vec.model")

# Ways to use the model
#输入与“自由”相近的n个词
n = 3
for key in model.wv.similar_by_word('自由', topn = n):
    print(key)


# req_count = 5
# for key in model.wv.similar_by_word('沙瑞金'.decode('utf-8'), topn =100):
#     if len(key[0])==3:
#         req_count -= 1
#         print key[0], key[1]
#         if req_count == 0:
#             break;