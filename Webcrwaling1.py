import pandas as pd
import sys
import io
from urllib.request import urlopen
from bs4 import BeautifulSoup

a = []

html = urlopen("https://finance.naver.com")
# print(html)
soup = BeautifulSoup(html, "lxml", from_encoding='utf-8')
# print(soup)
summary_info = soup.find('div', attrs={"class":"group_type is_active"})
# print(summary_info)
summary_info_list = summary_info.find_all('a')

for summary_info_line in summary_info_list:
    print(summary_info_line.text)
    print(type(summary_info_line.text))
    a.append(summary_info_line.text)

print(a)

df = pd.DataFrame(a)
# df = pd.read_csv(io.StringIO(summary_info_line.text))
print(df)
df.to_csv('/Users/verdfg/Desktop/Crwaling_pj.csv', mode='a')