#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
from pprint import pprint
import os
import pandas as pd
        
intro = """Les-Paul, SG, ES, Acoustic, Designer, Bass 를 'crl.run( )'안에 입력하세요.
입력한 값에 대한 깁슨 홈페이지에 있는 모든 깁슨 모델을 제공합니다."""
maker = 'jungho kang'

BASE_DIR = os.getcwd() # os명령어. get current work directory? 현재 작업 주소

class crl(object):
    # def __init__(self, base_dir = BASE_DIR):
    def __init__(self, base_dir):
        self.base_dir = BASE_DIR
    
    def run(model):
                 
        PICTURE_DIR = os.path.join(BASE_DIR, 'guitar_pictures_{}'.format(model))
        if not os.path.exists(PICTURE_DIR):
            os.makedirs(PICTURE_DIR) # 만약 경로가 없으면, 생성하겠습니다.
    
        guitar_list = [] # 새로운 빈 리스트를 생성합니다.
        gibson_usl = "https://www.gibson.com/Guitars/"+model 
# params = {
#     'Guitars': 'Guitars',
#     'Les-Paul': 'Les-Paul'
# }
# gibson_usl
        resp = requests.get(gibson_usl)
        soup = BeautifulSoup(resp.content, 'html.parser')
        gibson_contents = soup.find('div', class_='row pb-5').find_all('div', class_='col-sm-12 col-md-6 col-lg-4 px-2 mb-4')
# resp
# resp.content
# soup
# gibson_contents.content

        for div in gibson_contents:
            guitar_dict = {}

            a_tag = div.find('h4').find('a')
    # print(a_tag)
            guitar_dict['link'] = 'https://www.gibson.com'+a_tag['href']
            guitar_dict['name'] = a_tag.text
    # print(a_tag['href'])
    
            b_tag = div.find('div', class_='price-label ml-3').find('span')
            guitar_dict['price'] = b_tag.text
    # print(b_tag)
            guitar_list.append(guitar_dict)
    
            c_tag = div.find('img')
    # print(c_tag)
    # print(c_tag['src'])
    
            img_url = c_tag['src']
            img_resp = requests.get(img_url)
    # img_url
    # imgresp.content
            p_filename = img_url.split('/')[-4:]
            filename = "".join(p_filename)
    # filename
    
            guitar_picture_path = os.path.join(PICTURE_DIR, filename)  
            with open(guitar_picture_path, 'wb') as f:
                f.write(img_resp.content)
    
    # fix plz
    # detail_resp = requests.get('https://www.gibson.com'+a_tag['href'])
    # detail_soup = BeautifulSoup(detail_resp.content, 'html.parser')
    # detail_soup
    # detail_contents = soup.find('div', class_='gibson-card py-4')
    # detail_contents
    
        
        return guitar_list

