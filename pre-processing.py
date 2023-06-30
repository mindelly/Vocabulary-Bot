import requests
from bs4 import BeautifulSoup
import csv
import os


path = os.getcwd()
file_name = 'words.csv'
file_path = path + '/' + file_name


headers = {
'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36', 
           }


link = 'https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000/'
domain = "https://www.oxfordlearnersdictionaries.com"
content = requests.get(link, headers=headers)
soup = BeautifulSoup(content.text, features="html.parser")
list_li = soup.find_all('ul', {'class':'top-g'})[0].find_all('li')


header_row = ['word', 'level', 'word_url', 'word_class']

with open(file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(header_row)

    for li in list_li:
        try:
            word = li.find_all('a')[0].text
            level = li['data-ox5000']
            word_url = domain + li.find_all('a')[0]['href']
            word_class = li.find_all('span')[0].text

            row = [word, level, word_url, word_class]
            csv_writer.writerow(row)
            
        except KeyError:
            row = [word, None, word_url, word_class]
            csv_writer.writerow(row)
            print(li)
