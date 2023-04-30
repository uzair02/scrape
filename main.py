from bs4 import BeautifulSoup
import requests
import pandas as pd

#function to scrape
def myScrapy(url, tagName, className):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    res = soup.find_all(tagName, {'class': className})
    pList = []
    for i in res:
        pList.append(i.get_text())
    print("scraped Successfully!")
    return pList

url = input("Enter url you want to scrape: ")
tName = input("Enter tag name: ")
cName = input("Enter class name: ")
fName= input("Enter file name: ")

data = myScrapy(url, tName, cName)

#making csv file of scraped data
df = pd.DataFrame(data, columns=["Data"])
df.to_csv(fName,".csv", index=False)