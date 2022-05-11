"""
Description: 匹配相似文档
Author: TpunkT
Time: Fri Apr 29 2022 15:25:27 GMT+0800 
"""

from similar_by_gensim import get_art_by_gensim
from re_deal_html import get_links, get_doc
from similar_by_sklearn import get_art_by_sk
from txt_handle import *

# 源文件获取地址及选择器
org = {
  'url': 'https://www.163.com/dy/article/H6GI9USS0514R9M0.html?clickfrom=w_yw',
  'selector':'div.post_body',
  'content': ''
}

# 需要匹配网站地址及选择器
compare = {
  'url': 'https://www.sohu.com/',
  'selector':'body',
  'subSelector': 'div.text'
}

if __name__ == '__main__':

  # 获取org文件内容
  org['content'] = get_doc(org['url'], org['selector'])
  
  # 提取内容中的超链接
  links = get_links(compare['url'],compare['selector'], 'editor')

  # 方式一
  get_art_by_gensim(links,org,compare,0.6) 
  
  # 方式二
  get_art_by_sk(links,org,compare,0.6)