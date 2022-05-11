from xml import dom
from bs4 import BeautifulSoup
import urllib3
import requests
import re

# 通过url 获取html内容
def get_target_content(url,position):
  try:
    resp = requests.get(url)
    if resp.status_code == 200:
      soup = BeautifulSoup(resp.text, 'lxml')
    ele = soup.select(position)
    if isinstance(ele,list) & len(ele)>0 :
      return ele[0].text.strip()
    else:
      return ''
  except Exception as e:
    print (e)
    return ''

# 通过url 获取html内容
def  get_html(url): 
  userAgent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
  http = urllib3.PoolManager(timeout=2)
  response = http.request('get', url, headers={'User_Agent': userAgent})
  html = response.data
  return html

# 通过url 地址 来获取 页面的BeatifulSoup对象
def get_soup(url):
  if not url:
    return None
  try:
    soup = BeautifulSoup(get_html(url), 'lxml')
  except Exception as e:
    print (e)
    return None
  return soup

# 获取页面的超链接
def get_links(url,selector,finishedContents = []):
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
      #过滤已完成集合
      elif link in finishedContents:
        pass
      elif 'article' in link:
        result.append(link)
  return result
