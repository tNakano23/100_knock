import pandas as pd
df = pd.read_table("2/popular-names.txt", header=None)
N = 5

print(df[:N])
print(df.head(N))

# どちらも同じ
#            0  1     2     3
# 0       Mary  F  7065  1880
# 1       Anna  F  2604  1880
# 2       Emma  F  2003  1880
# 3  Elizabeth  F  1939  1880
# 4     Minnie  F  1746  1880


#UNIXコマンド
# $head -n 5 popular-names.txt
