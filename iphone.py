import requests
from bs4 import BeautifulSoup
from csv import writer
import pandas as pd

url = "https://www.flipkart.com/search?q=iphones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

r = requests.get(url)

soup = BeautifulSoup(r.content,"html.parser")
lists = soup.find_all("div", class_="_1AtVbE col-12-12")


with open("iphone.csv","w",encoding ="utf8",newline = "") as f:
    thewriter = writer(f)
    header =["Name","Rom","Screen","Camera","Chip","Processor","Price"]
    thewriter.writerrow(header)
    for list in lists:
        name = list.find("div",class_="_4rR01T")
        if name == None:
            pass
        else:
            l = [name.text]
            for i in range(4):
                l.append(list.find("ul",class_="_1xgFaf").findChildren()[i].text)
            l.append(list.find("div",class_="_30jeq3 _1_WHN1").text)
            thewriter.writerrow(l)
df = pd.read_csv("iphone.csv")
df.head()