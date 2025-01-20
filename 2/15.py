import pandas as pd
df = pd.read_table("2/popular-names.txt", header=None)
N = 5

print(df[-N:])
print(df.tail(N))

# どちらも同じ
#              0  1      2     3
# 2775  Benjamin  M  13381  2018
# 2776    Elijah  M  12886  2018
# 2777     Lucas  M  12585  2018
# 2778     Mason  M  12435  2018
# 2779     Logan  M  12352  2018


#UNIXコマンド
# $tail -n 5 popular-names.txt