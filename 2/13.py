import pandas as pd

col1 = pd.read_csv("col1.txt", header=None)
col2 = pd.read_csv("col2.txt", header=None)

col1_2 = pd.concat([col1, col2], axis=1)
col1_2.to_csv("col1_2.txt", sep="\t", header=False, index=False)

#UNIXコマンド
# $paste col1.txt col2.txt > col1_2.txt

print(col1_2)
print(type(col1_2))

#               0  0
# 0          Mary  F
# 1          Anna  F
# 2          Emma  F
# 3     Elizabeth  F
# 4        Minnie  F
# ...         ... ..
# 2775   Benjamin  M
# 2776     Elijah  M
# 2777      Lucas  M
# 2778      Mason  M
# 2779      Logan  M

# [2780 rows x 2 columns]
# <class 'pandas.core.frame.DataFrame'>



# ======================


# paste  -d"!@" names places dates > npd
# ↓
# rachel!New York@February 5
# jerry!Austin@March 13
# mark!Chicago@June 21
# marsha!Boca Raton@July 16
# scott!Seattle@November 4