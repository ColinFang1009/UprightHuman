# process the file with jieba to stop words
import jieba
import jieba.analyse
from gensim.test.utils import common_texts, get_tmpfile
import gensim.models
from gensim.models import word2vec, Word2Vec 
import gensim

# use this command to allow JIEBA to recognize specific words desired.
# many more words can be added
jieba.suggest_freq('人民', True)
jieba.suggest_freq('自由', True)
jieba.suggest_freq('政府', True)


# read and process our text.
file_path = './1948.txt'
with open(file_path,encoding='utf-8') as f:
    document = f.read()
    document_cut = jieba.cut(document)
    result = ' '.join(document_cut)
    with open(file_path, 'w',encoding="utf-8") as f2:
        f2.write(result)

f.close()
f2.close()
#at the end of the command, the .txt file is successfully processed/stopped.
sentences = word2vec.LineSentence(file_path)
#训练语料
path = get_tmpfile("word2vec48.model") #创建临时文件
model = word2vec.Word2Vec(sentences, hs=1,min_count=1,window=10,size=100)
model.save("word2vec48.model")