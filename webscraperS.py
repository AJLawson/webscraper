from bs4 import BeautifulSoup
import requests, string, random
from collections import Counter

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

count = 0
names = []

def get_price(url):
    global count, names
    count += 1
    if count > 10:
        return
    r = requests.get(url)
    html = BeautifulSoup(r.text)#, "html5lib")
    price = html.find(id="priceblock_ourprice")
    
    name = html.find(id="productTitle")
    title = list(name)
    title1 = title[0].split()
    title2 = ""
    for i in range(len(title1)):
        title2 = title2 + title1[i] + " "
    
    names.append((title2, float(price.text[1:])))
    print(title2 + price.text + " ")
    item = str(random.randint(0,3))
    linkdiv = html.find('th', {"class":"comparison_image_title_cell comparable_item"+item})
    link = ""
    try:
        link = linkdiv.findAll('a', {"class":"a-link-normal"})[0]
    except:
        return
    #print(link['href'])
    get_price("https://amazon.com" + link['href'])

def plot_words():
    titles = []
    prices = []
    for (n, p) in names:
        titles.append(n)
        prices.append(p)
    
    index = np.arange(len(titles))
    
    fig = plt.figure()
    plt.bar(index, prices)
    plt.xticks(index, titles, rotation="vertical", size="x-small")
    fig.savefig("Guitar Prices")
    

get_price("https://smile.amazon.com/Fender-Acoustic-Strings-Instructional-Polishing/dp/B0092V7WJ0/ref=sr_1_4?ie=UTF8&qid=1517172902&sr=8-4&keywords=acoustic+guitar")
plot_words()