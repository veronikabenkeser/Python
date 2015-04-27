import requests
from bs4 import BeautifulSoup

#core spider

def browse_spider():
    resultingList=[]
    url = "http://www.ewg.org/skindeep/search.php?query=+"
    soup = BeautifulSoup(get_text(url))
    section = soup.findAll('div', {'class':'row'})
    for div in section:
        links=div.findAll('a')
        for a in links: #list of category name and category link
            ls0=[]
            category = a.text #vs a.contents returns a list
            href = "http://www.ewg.org" + a.get('href')
            ls0.append(category)
            ls0.append(href)
            resultingList.append(ls0)

    for item in resultingList:
        item[1] = get_items(item[1])
        #foreach link : pull , score and price
        for link in item[1]:
            soup=BeautifulSoup(get_text(link))

            #get price for each item
            priceLinks = links_in_soup(soup, 'div', {'id':'Where_to_Purchase'}, "")
            print(priceLinks)

            #get score for each item
            section = soup.findAll('div', {'class':'scoretextbg'})
            for div in section:
                score = div.findAll('img')

def get_text(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    return plain_text

def links_in_soup(soup, html_element, attrs, b):
    result=[]
    section = soup.findAll(html_element, attrs)
    for html_element in section:
        links = html_element.findAll('a')
        for a in links:
            href= b +a.get('href')
            result.append(href)

    return result

#get links from each category and group the links based on the category
def get_items(url):
    #go to this link and get all the links on this page

    soup = BeautifulSoup(get_text(url))

    links = links_in_soup(soup, 'td', {'class':'product_name_list'}, "http://www.ewg.org")

    return links
