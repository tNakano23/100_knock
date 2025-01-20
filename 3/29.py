import requests
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

mydict = {}
ptn = [
    "'{2,5}",
    "\]{1,2}",
    "\[{1,2}",
    "#REDIRECT",
    "~~~~",
    "<!--\s",
    "\s-->",
    "={2,6}\s",
    "=\s{2,6}",
    "[\*,#]*\s",
    "----",
    "\{\{",
    "\}\}",
    "",
]

def resub_multi_ptn(ptn, str):
    for i in range(len(ptn)):
        str = re.sub(ptn[i], "", str)
    return str

for text in uk_texts:
    match = re.search("\|(.+?)\s=\s(.+)",text)
    if match:
        sub_bold = match.group(2)
        sub_bold = resub_multi_ptn(ptn, sub_bold)
        mydict[match.group(1)]=sub_bold

for i in mydict:
    # print(i, "=" ,mydict[i])
    pass

S = requests.Session()

URL = "https://www.mediawiki.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "titles": f"File:{mydict['国旗画像']}",
    "iiprop":"url"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()
PAGES = DATA["query"]["pages"]

for k, v in PAGES.items():
    print(v["imageinfo"][0]["url"])
