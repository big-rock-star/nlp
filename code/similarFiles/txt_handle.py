
import os

def wirte_txt(src,content,type = 'a'):
  f = open(src,mode=type,encoding='utf8')
  f.write(content)
  f.close()

def read_txt(src):
  return open(src, "r",encoding='utf8').read()

def getArtName(link):
  return link.split('/')[-1].split('.html')[0]

def get_allfile(path):  # 获取所有文件
    all_file = []
    for f in os.listdir(path):  #listdir返回文件中所有目录
        f_name = os.path.join(path, f)
        all_file.append(f_name)
    return all_file