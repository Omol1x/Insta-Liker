from os import path, walk
from queue import Queue
from threading import Thread
from time import sleep
import click
from js2py import eval_js

q = Queue()
convert = eval_js(r'function convert(t){let l=[],n=t.split("\n");return n.forEach(function(e,t){e=e.split("\t");if(7==e.length){let t={};t.domain=e[0],t.httpOnly="TRUE"===e[1],t.path=e[2],t.secure="TRUE"===e[3];let n=e[4];17==n.length&&(n=Math.floor(n/1e6-11644473600)),t.expirationDate=parseInt(n),t.name=e[5],t.value=e[6],l.push(t)}}),JSON.stringify(l,null,2)}')

def get_cookies():
    global c
    c=0
    cookies = []
    for root, dirs,files in walk(path.join('cookies'),topdown=False):
        for file  in files:
            if '.txt' in file.lower():
                c+=1;cookies.append(root+'/'+file)
    return cookies

def convert_cookie(i):
        cookieFile = q.get()
        try:
            cookie = open(cookieFile,'r+',encoding='utf8',errors='ignore').read()
            cookie = str(convert(cookie))
            open(cookieFile.replace('.txt','.json'),'w').write(cookie) 
        except:pass
        q.task_done()
def main_convert():
    global bar
    cookies = get_cookies()
    for cookieFile in cookies:q.put(cookieFile)
    for i,cookieFile in enumerate(cookies):sleep(0.1),Thread(target=convert_cookie,args=(i,)).start()
    q.join()