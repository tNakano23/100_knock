import pandas as pd
df = pd.read_table("2/popular-names.txt", header=None)

df_sort = df.sort_values(2, ascending=False)
print(df_sort)

#UNIXコマンド
# $cut -f 3  popular-names.txt | sort -n -r
