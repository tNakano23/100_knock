import pandas as pd
import re

path = "3/jawiki-country.json"
df = pd.read_json(path, lines=True)
uk_df = df[df["title"]=="イギリス"]
uk_texts = uk_df["text"].values

# print(type(uk_texts))   #<class 'numpy.ndarray'>
# print(len(uk_texts))    #1

uk_texts = uk_texts[0].split("\n")

# print(type(uk_texts))   #<class 'list'>
# print(len(uk_texts))    #689

for text in uk_texts:
    match = re.search("ファイル:(.+?)\|",text)
    if match:
        print(match.group(1))


"""
Royal Coat of Arms of the United Kingdom.svg
Descriptio Prime Tabulae Europae.jpg
Lenepveu, Jeanne d'Arc au siège d'Orléans.jpg
London.bankofengland.arp.jpg
Battle of Waterloo 1815.PNG
Uk topo en.jpg
BenNevis2005.jpg
Population density UK 2011 census.png
2019 Greenwich Peninsula & Canary Wharf.jpg
Leeds CBD at night.jpg
Palace of Westminster, London - Feb 2007.jpg
Scotland Parliament Holyrood.jpg
Donald Trump and Theresa May (33998675310) (cropped).jpg
Soldiers Trooping the Colour, 16th June 2007.jpg
City of London skyline from London City Hall - Oct 2008.jpg
Oil platform in the North SeaPros.jpg
Eurostar at St Pancras Jan 2008.jpg
Heathrow Terminal 5C Iwelumo-1.jpg
UKpop.svg
Anglospeak.svg
Royal Aberdeen Children's Hospital.jpg
CHANDOS3.jpg
The Fabs.JPG
Wembley Stadium, illuminated.jpg
"""