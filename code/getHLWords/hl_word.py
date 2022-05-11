from nltk import *
import jieba
import jieba.posseg  as ps
from collections import Counter


# 文本处理
def textParse(str_doc):
  str_doc = re.sub('\u3000','',str_doc)
  str_doc = re.sub('\s+',' ',str_doc)
  str_doc = re.sub('\d',' ',str_doc)
  str_doc = str_doc.replace('\n', ' ')
  
  return str_doc

# jieba之后的文字进行过滤
def rm_tokens(words,stwlist):
  word_list = list(words) # 将切完的值转化成列表
  stop_words = stwlist

  for i in range(word_list.__len__())[::-1]: # -1表示数组最后一项
    if word_list[i] in stop_words: # 去除停用词 
      word_list.pop(i)
    elif word_list[i].isdigit(): # 去除数字
      word_list.pop(i)
    elif len(word_list[i]) == 1: # 去除单个字符
      word_list.pop(i)
    elif  word_list[i] == ' ': # 去除空格
      word_list.pop(i)
  
  return word_list


# 利用jieba依次对文本进行拆分
def seg_doc(str_doc ,paddle):
  sent_list = str_doc.split('/n')
  sent_list = map(textParse,sent_list)

  # 分词并去除停用词并合并
  word_2dlist = sum([rm_tokens(jieba.cut(part,cut_all=False),[]) for part in sent_list],[])
  featword = extract_featrue(str_doc,paddle)
  word_2dlist = extract_words(word_2dlist,featword)

  return word_2dlist

# 获取指定类型的特征词
def extract_words(wordlist ,featword):
  words = []
  for word in wordlist:
    if word in featword:
      words.append(word)

  return words

# 获取所有的特征词
def extract_featrue(str_doc,paddle):
  featword = []

  #用户自定义特征词性列表
  user_pos_list = [paddle]
  for word, pos in ps.cut(str_doc):
    if pos in user_pos_list:
      if word + ' ' + pos + '\n' not in featword:
        featword.append(word)

  return featword

def nltk_wf_featrue(word_list,count):
  # fdist = FreqDist(word_list)
  # print('=','频率分布表','=')
  # fdist.tabulate(count)

  words = Counter(word_list)
  print (words.most_common(count))

def get_word_list(str_doc,paddle,count):
  word_list = seg_doc(str_doc,paddle)
  nltk_wf_featrue(word_list,count)
