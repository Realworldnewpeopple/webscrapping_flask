from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import Request, urlopen
from PIL import Image
import io
from tqdm import tqdm
import time
from os import listdir
from os.path import isfile, join
import re
from functools import reduce
from operator import add
import re

def save_link(soup):
    image_link = []
    for i in tqdm(range(0, len(soup.find_all('img'))), desc="first"):
        if len(soup.find_all('img')[i]['src'])>5:
            if re.search('http',soup.find_all('img')[i]['src'].lower()):
                image_link.append(soup.find_all('img')[i]['src'])
            else:
                continue
        else:
            continue
    return image_link

def anime(webpage):
    list_links=[]
    for lists in webpage:
        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Chrome(options=chrome_options, executable_path='./Driver/chromedriver.exe')
            driver.get(lists)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            list_links.append(save_link(soup))
        except:
            continue
    list_links=list(set(reduce(add,list_links)))
    return list_links

def save_img(image_link):
    for j in tqdm(range(0,len(image_link)),desc="second"):
        if re.search('http',image_link[j].lower()):
            try:
                req = Request(image_link[j], headers={'User-Agent': 'Mozilla/5.0'})
                web_byte = urlopen(req).read()
                image = Image.open(io.BytesIO(web_byte))
                filename=image_link[j].split('/')[-1].split('.')[0]
                if "%" in filename:
                    filename=re.sub('%','-',filename)
                image.save("./static/img/" + filename + ".jpg")
                time.sleep(5)
            except:
                continue


def image_link(mypath):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    link=[mypath+"/"+i for i in onlyfiles]
    return link



