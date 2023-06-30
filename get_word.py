import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
from config import headers

def pick_word(ext_level):
    words = pd.read_csv('words.csv')

    if ext_level != 'random':
        words = words[words.level == ext_level].copy()

    size_words = len(words)
    number = random.randint(0, size_words)

    word_url = words.loc[number,'word_url']
    word = words.loc[number,'word']
    level = words.loc[number,'level']
    word_class = words.loc[number,'word_class']

    content = requests.get(word_url, headers=headers)
    soup = BeautifulSoup(content.text, features="html.parser")
    def_soup = soup.find_all('span', {'class':"def"})
    examples_soup = soup.find_all('ul', {'class':"examples"})


    dic = dict()
    num = 0
    for defin, examples in zip(def_soup, examples_soup):
        num += 1
        ex_list = [e.text for e in examples.find_all('li')]
        dic[str(num)+ ' '+ defin.text] = ex_list

    if len(examples_soup) != len(def_soup):
        for i in range(len(examples_soup), len(def_soup)):
            num +=1
            dic[str(num)+ ' ' + def_soup[i].text] = list()
    
    return dic, word, level, word_class


