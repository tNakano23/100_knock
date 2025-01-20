import pandas as pd
df = pd.read_table("2/popular-names.txt", header=None)
print(df.shape[0])

# 2780


path = r'2\popular-names.txt'
with open(path) as f:
    lst = f.readlines()
print(len(lst))

# 2780


# ----------------
#UNIXコマンド
# $ wc -l 2/popular-names.txt
# 2780 2/popular-names.txt