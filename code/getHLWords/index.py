import time
from re_deal_html import get_target_content,get_links
from txt_handle import wirte_txt,read_txt
from hl_word import get_word_list

url = 'https://news.163.com/domestic/'
list_selector = 'body > div.second2016_wrap.guonei_second_wrap > div.second2016_content > div.ns_area.second2016_main.clearfix > div.second_left'

content_selector = 'div.post_main'
content_url = './content.txt'

if __name__ == '__main__':
  startTime = time.time()

  # 1. 提取内容中的超链接
  links = get_links(url,list_selector)
  print(links,'/n', 'totle:', len(links))

  # 2. 清空文件
  wirte_txt(content_url,'','w')

  # 3. 存储的目标文本中的内容
  for src in links:
    wirte_txt(content_url,get_target_content(src, content_selector))
  
  # 4. 做分词处理 提取 人名 地点 等信息
  content = read_txt(content_url)
  get_word_list(content, 'nr',5)
  get_word_list(content, 'ns',5)
  get_word_list(content, 'nt',5)

  endTime = time.time()
  print ('Total spent times:%.2f' % (endTime - startTime) + 's')