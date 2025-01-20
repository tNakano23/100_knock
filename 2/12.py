import pandas as pd
df = pd.read_table("2/popular-names.txt", header=None)
df1 = df.iloc[:, 0]
df2 = df.iloc[:, 1]

df1.to_csv("2/col1.txt", sep=",", header=False, index=False)
df2.to_csv("2/col2.txt", sep=",", header=False, index=False)


#UNIXコマンド
# $cut -f 1 popular-names.txt > col1.txt
# $cut -f 2 popular-names.txt > col2.txt