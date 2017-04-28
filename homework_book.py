# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests , re , json
from collections import Counter

def book_info(div):
 """given a BeautifulSoup <td> Tag representing a book,
 extract the book's details and return a dict"""
 author = div.find("div", "box_mid_billboard_pro").p.text
 title = div.find("h3").a.text
 price = div.find("span","price").text

 return {
 "author" : author,
 "title" : title,
 "price" : price,
 }

url = "http://www.eslite.com/newbook_list.aspx?cate=156&sub=159&page=1"
soup = BeautifulSoup(requests.get(url).text, 'html5lib')


tds = soup('td', 'thumbtext')
print len(tds)
# 30

def is_video(td):
 """it's a video if it has exactly one pricelabel, and if
 the stripped text inside that pricelabel starts with 'Video'"""
 pricelabels = td('span', 'pricelabel')
 return (len(pricelabels) == 1 and
 pricelabels[0].text.strip().startswith("Video"))
#print len([td for td in tds if not is_video(td)])
# 21 for me, might be different for you

from time import sleep
base_url = "http://www.eslite.com/newbook_list.aspx?cate=156&sub=159&page="
books = []
NUM_PAGES = 10 # at the time of writing, probably more by now
for page_num in range(1, NUM_PAGES + 1):
 # print "souping page", page_num, ",", len(books), " found so far"
 url = base_url + str(page_num)
 soup = BeautifulSoup(requests.get(url).text, 'html5lib')
 for div in soup('div', 'box_mid_billboard'):
     if not is_video(div):
        books.append(book_info(div))
     #date = div.find("span").text.strip()
     #print date
 # now be a good citizen and respect the robots.txt!
# sleep(2)

print(books)
price= []
for b in books:
    print("title : " + b['title'])
    print("author : " + b['author'])
    print("price : " + b['price'])

print(len(books))




# def get_year(book):
#     """book["date"] looks like 'November 2014' so we need to
#     split on the space and then take the second piece"""
#     return int(book["date"].split()[1])
# # 2014 is the last complete year of data (when I ran this)
# year_counts = Counter(get_year(book) for book in books
#     if get_year(book) <= 2017)
import matplotlib.pyplot as plt
# years = sorted(year_counts)
# book_counts = [year_counts[year] for year in years]
# plt.plot(years, book_counts)
# plt.ylabel("# of data books")
# plt.title("Data is Big!")
# plt.show()




