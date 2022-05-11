# coding: utf-8

# from imp import reload
from numpy import mat
from stop_words import *
from re_deal_html import get_doc

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer

def get_art_by_sk(links,org,compare,similarity_val) :
  for i,src in enumerate(links):
    corpus = [
      org['content'],
      get_doc(src, compare['subSelector'])
    ];
    # print('corpus===',corpus)

    try:
      # max_df 表示这个词如果在整个数据集中超过95%的文本都出现了，那么我们也把它列为临时停用词
      # min_df 与max_df相反，虽然文档频率越低，似乎越能区分文本，可是如果太低，例如10000篇文本中只有1篇文本出现过这个词，仅仅因为这1篇文本，就增加了词向量空间的维度，太不划算
      # 计算词频 max_df=0.95, min_df=2, 
      tfidf_vectorizer = TfidfVectorizer(min_df=2, stop_words= stop_words)
      # 统计每个词语的tf-idf权值
      transformer=TfidfTransformer()
      ##第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵
      # print('tfidf_vectorizer.fit_transform(corpus)===',tfidf_vectorizer.fit_transform(corpus))
      tfidf= transformer.fit_transform(tfidf_vectorizer.fit_transform(corpus))

      # print('tfidf===',mat(tfidf))
      
      similaritie = (tfidf * tfidf.T).A[0][1]


      # print('similaritie===',similaritie)
      if ( similaritie >= similarity_val ):
        print('sklearn:','\n', 'link=',src,'\n','相似度为',round(similaritie,2))
        break 
    except Exception as e :
      print('e====',e)
      pass

   
      
  