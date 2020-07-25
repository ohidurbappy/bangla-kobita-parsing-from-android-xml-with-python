from bs4 import BeautifulSoup

import glob

names=glob.glob('*.xml')

f=open("output.txt",'w',encoding='utf-8')


for f_name in names:
    
    src=open(f_name,encoding='utf-8')

    soup=BeautifulSoup(src.read(),'lxml')

    src.close()

    e=soup.select('TextView')

    for a in e:
        print(a['android:text'])

     
        f.write(a['android:text'])



f.close()
