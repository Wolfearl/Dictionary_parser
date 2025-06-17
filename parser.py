from bs4 import BeautifulSoup
import requests
import pandas as pd


url = "https://informatics.ru/blog/zhaba-kryakozyabry-i-kostyl-slovar-terminov-programmistov/"
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

wrapper = soup.find("div", class_="content__wrapper")
main_data = wrapper.find_all('p')[1:-2]
dictionary = []
for m in main_data:
    if m.get_text(strip=True):
        string = m.text.split('—')
        dictionary.append([string[0].strip(), string[1].strip()])

# for key, index in dictionary.items():
#     print(key, index)
df = pd.DataFrame(dictionary, columns=['Слово', 'Определение'])
df.to_excel("dictionary.xlsx", index=False)



