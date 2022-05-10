
def wirte_txt(src,content,type = 'a'):
  f = open(src,mode=type,encoding='utf8')
  f.write(content)
  f.close()

def read_txt(src):
  return open(src, "r",encoding='utf8').read()