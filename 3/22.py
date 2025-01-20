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
    match = re.search("\[Category:(.*(?!|\*))\]\]", text)
    if match:
        print(match.group(1))

# ~~~

for text in uk_texts:
    if re.search("Category", text):
        text = text.replace("[[Category:", "").replace("|*]]", "").replace("]]", "")
        print(text)

"""どちらも
イギリス|*
イギリス連邦加盟国
英連邦王国|*
G8加盟国
欧州連合加盟国|元
海洋国家
現存する君主国
島国
1801年に成立した国家・領域
"""
