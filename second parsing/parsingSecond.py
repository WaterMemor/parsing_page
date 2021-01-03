import requests
import pandas as pd
from pandas import read_excel
from bs4 import BeautifulSoup
import locale
import shutil
import os.path
# myLocale=locale.setlocale(category=locale.LC_ALL, locale="ru_RU.UTF-8")
dir='C:\\Users\\Nastya\\Desktop\\newphotos\\picc9\\'
file=dir+'Simbut.xls'
df = read_excel(file)#, sheet_name = '1'
foto=df['Foto'].tolist()
df1 = pd.DataFrame(columns = ['COL1'])

index=1
for f in foto:
    url=str(f)
    print('url ',url)
    if url.find('http')<0: continue
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser') #Отправляем полученную страницу в библиотеку для парсинга
    span=soup.select_one('span.product__options-item-value > a')
    iter=0
    for i in span:
        df1 = df1.append([i])
df1.to_excel('C:\\Users\\Nastya\\Desktop\\newphotos\\picc9\\3.xlsx')
print('STOP')