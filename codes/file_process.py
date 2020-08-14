# process the file with jieba to stop words
import jieba
import jieba.analyse

# use this command to allow JIEBA to recognize specific words desired.
# many more words can be added
jieba.suggest_freq('人民', True)
jieba.suggest_freq('自由', True)
jieba.suggest_freq('政府', True)


# read and process our text.
with open('./demo.txt') as f:
    document = f.read()
    
    #document_decode = document.decode('GBK')
    
    document_cut = jieba.cut(document)
    #print  ' '.join(jieba_cut)  //如果打印结果，则分词效果消失，后面的result无法显示
    result = ' '.join(document_cut)
    result = result.encode('utf-8')
    with open('./demo.txt', 'w') as f2:
        f2.write(result)
f.close()
f2.close()
#at the end of the command, the .txt file is successfully processed/stopped.