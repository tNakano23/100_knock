import pandas as pd

path = "3/jawiki-country.json"
df = pd.read_json(path, lines=True)
# df2 = pd.read_json(path)

uk_df = df[df["title"]=="イギリス"]
uk_texts = uk_df["text"].values

print(uk_texts)

