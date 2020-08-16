import jieba
import jieba.analyse

#file position, pre-processing
#for loop to preprocess multiple txt files
# for i in range(2003, 2004):
    # year = str(i)
year = "2003-2"
file_path = './{}.txt'.format(year)
with open(file_path,encoding='utf-8') as f:
    document = f.read()
    document_cut = jieba.cut(document)
    result = ' '.join(document_cut)
with open(file_path, 'w',encoding="utf-8") as f2:
    f2.write(result)