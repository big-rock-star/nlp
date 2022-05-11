from xml import dom
from bs4 import BeautifulSoup
import urllib3
import requests
import re

headers = {
 'User-gent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}

# 通过url 获取html内容
def get_doc(url,selector):
  ele = []
  try:
    resp = requests.get(url,headers=headers)
    if resp.status_code == 200:
      soup = BeautifulSoup(resp.text, 'lxml')
      ele = soup.select(selector)
    if isinstance(ele,list) & len(ele) > 0 :
      return ele[0].text.strip()
    else:
      return ' '
  except Exception as e:
    print (e)
    return ' '

# 通过url 获取html内容
def get_html(url): 
  content = ''
  resp = requests.get(url,headers=headers)
  if resp.status_code == 200:
    content = resp.text
  return content

# 获取页面的超链接
def get_links(url,selector,match_str):
  soup = BeautifulSoup(get_html(url), 'lxml')
  soup.select(selector)
  # 集合
  result = []

  # 非法URL 1
  invalidLink1 = '#'
  # 非法URL 2
  invalidLink2 = 'javascript:void(0)'
  #查找文档中所有a标签
  for k in soup.find_all('a'):
    #查找href标签
    link = k.get('href')
    # 过滤没找到的
    if (link is not None):
      #过滤非法链接
      if link == invalidLink1:
        pass
      elif link == invalidLink2:
        pass
      elif link.find("javascript:") != -1:
        pass
      elif match_str in link:
        result.append('https://www.sohu.com' + link)
  return result
