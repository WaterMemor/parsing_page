import requests
from pandas import read_excel
from bs4 import BeautifulSoup
import locale
import shutil
import os.path
# myLocale=locale.setlocale(category=locale.LC_ALL, locale="ru_RU.UTF-8")
dir='work\\picN\\'
file=dir+'Example.xlsx'
df = read_excel(file, sheet_name = '1')
foto=df['Foto'].tolist()
art=df['Art'].tolist()

index=1
for f in foto:
    url=str(f)
    print('url ',url)
    if url.find('http')<0: continue
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    images=soup.find_all('img') 
    iter=0
    for i in images:
        src=i.get('src')
        if src.find('upload')>0:
            art1= str(art[index-1])
            art1='sh'+art1.replace('.0','')
        
            source='http://photo.mirigr.by'+src
            destination=dir+str(art1)+'.jpg'
    
            print('source,', destination, ',destination')
            if not os.path.isfile(destination) :
                filereq = requests.get(source,stream = True)
                with open(destination,"wb") as receive:
                    shutil.copyfileobj(filereq.raw,receive)
                    del filereq
                iter=iter+1   
            break  
    index=index+1
