from re_deal_html import get_doc
from txt_handle import *
from hl_word import seg_doc
from gensim import corpora,models,similarities

def create_tfidf (org_content):
  texts = seg_doc(org_content)
  dictionary = corpora.Dictionary()

  # 同时对无需的数据做剔除
  dictionary.add_documents([texts])

  #特征数
  num_features = len(dictionary.token2id)

  # 生成词袋模型
  corpus = [dictionary.doc2bow(texts),[]] # idf = log(1/1) = 0 tfidf = tf * 0 = 0

  # 对语料库对tfidf模型进行训练
  tfidf = models.TfidfModel(corpus)
  # print('tfidf===',tfidf)

  # 获取源文件的tfidf
  org_tf = tfidf[corpus]

  # 通过TfIdf对整个语料库进行转换并将其编入索引，以准备相似性查询
  sparse_matrix = similarities.SparseMatrixSimilarity(org_tf, num_features)
  return dictionary,tfidf,sparse_matrix

def get_compare_tf(compare_text,dictionary,tfidf):
  compare_texts = seg_doc(compare_text)
  dictionary.add_documents([compare_texts])
  compare_file_bow = dictionary.doc2bow(compare_texts)
  compare_tf = tfidf[compare_file_bow]
  return compare_tf

def get_art_by_gensim(links,org,compare,similarity_val):
  dictionary,tfidf,sparse_matrix = create_tfidf(org['content'])  # create_tfidf(read_txt('./doc/1.txt'))
  
  # 循环对比
  for i,src in enumerate(links):
    # 获取对比文件的分词结果
    compare_content = get_doc(src, compare['subSelector']) # read_txt('./doc/2.txt') 

    # 获取对比文件的tfidf
    compare_tf = get_compare_tf(compare_content,dictionary,tfidf)

    similaritie = sparse_matrix.get_similarities(compare_tf)[0]
    
    # print('get_similarities===',sparse_matrix.get_similarities(compare_tf))

    # 获取文件相似度
    # print('src===',src,round(similaritie,2))
    if ( similaritie >=  similarity_val ):
      print('gensim:','\n', 'link=',src,'\n','相似度为',round(similaritie,2))
      break
  