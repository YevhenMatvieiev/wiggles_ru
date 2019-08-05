import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

# Your directory
DIRECTORY = 'F:/bear'
# there are 666 strips
pages = (667)
url = 'http://neilswaab.ru'

os.makedirs(DIRECTORY, exist_ok=True)

for i in range(1, pages):
    page_url = urljoin(url, '?p=' + str(i))
    page_content = requests.get(page_url).text
    page_soup = BeautifulSoup(page_content, 'lxml')
    header = page_soup.find('h2')
    images = page_soup.find_all('img', class_=None)
    for j in images:
        if 'png' in j.attrs['src']:
            pic_link = j.attrs['src']
            print(pic_link)
    name_for_file = header.text
    # forbiden filename characters
    for c in '/\:*"?':
        if c in name_for_file:
            name_for_file = name_for_file.replace(c, "")
    with open(os.path.join(DIRECTORY, str(i) + '_' +  name_for_file + '.png'), 'wb') as file:
        print(file.name)
        file_content = requests.get(pic_link)
        file_content = file_content.content
        file.write(file_content)






