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
    if re.search("Category", text):
        print(text)

"""
{{Sisterlinks|commons=United Kingdom|commonscat=United Kingdom|s=Category:イギリス|n=Category:イギリス|voy=United Kingdom}}
[[Category:イギリス|*]]
[[Category:イギリス連邦加盟国]]
[[Category:英連邦王国|*]]
[[Category:G8加盟国]]
[[Category:欧州連合加盟国|元]]
[[Category:海洋国家]]
[[Category:現存する君主国]]
[[Category:島国]]
[[Category:1801年に成立した国家・領域]]
"""
