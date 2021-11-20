import requests
from bs4 import BeautifulSoup
try:
    url = "https://letssolvein.wordpress.com"
    r = requests.get(url)
    htmlcontent = r.content
    soup = BeautifulSoup(htmlcontent,'html.parser')
    #print(soup.prettify)
    #title = soup.title
    #print(title)
    #tags = soup.find('p')['class']
    #print(tags)
    #print(soup.find('p').get_text())
    anchors = soup.find_all('a')
    all_links = set()
    for link in anchors:
        if(link.get('href') !='#'):
            all_links.add("https://letssolvein.wordpress.com"+link.get('href'))
    print(all_links)

except Exception as e:
    print(e)
