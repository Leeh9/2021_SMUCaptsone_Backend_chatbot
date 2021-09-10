from gensim.models import doc2vec, Doc2Vec
from gensim.models.doc2vec import TaggedDocument
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import nltk
import jpype
from konlpy.tag import Kkma


d2v_psy = Doc2Vec.load('d2v_psy.model')
psyconsult = pd.read_csv('wellness.csv',encoding='CP949')

kkma = Kkma()
filter_kkma = ['NNG',  #보통명사
             'NNP',  #고유명사
             'OL' ,  #외국어
            ]

def tokenize_kkma(doc):
    jpype.attachThreadToJVM()
    token_doc = ['/'.join(word) for word in kkma.pos(doc)]
    return token_doc

def tokenize_kkma_noun(doc):
    jpype.attachThreadToJVM()
    token_doc = ['/'.join(word) for word in kkma.pos(doc) if word[1] in filter_kkma]
    return token_doc

def bot_answer(input):
    # 테스트하는 문장도 같은 전처리를 해준다.
    tokened_test_string = tokenize_kkma_noun(input)
    print('유저 입력: ' + (input))  #str(tokened_test_string)
    topn = 3
    test_vector = d2v_psy.infer_vector(tokened_test_string)
    result = d2v_psy.docvecs.most_similar([test_vector], topn=topn)
    answer_list = []

    for i in range(topn):
        print("{}위. {}, {} {} {}".format(i + 1, result[i][1], result[i][0], psyconsult['유저'][result[i][0]], psyconsult['챗봇'][result[i][0]]))
        answer_list.append(dict(acc=result[i][1], question=psyconsult['유저'][result[i][0]], answer=psyconsult['챗봇'][result[i][0]])) 

    return psyconsult['챗봇'][result[0][0]]