from bs4 import BeautifulSoup

html_code = '<a href="https//google.com" class="my_link">Go to Google</a>'

soup = BeautifulSoup(html_code,'html.parser')
r = soup.find('a',class_="my_link")
