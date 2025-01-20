import pandas as pd
df = pd.read_table("2/popular-names.txt", header=None)

# print(df[0])
# print(df.iloc[:, 0])
print(set(df.iloc[:, 0]))
# print(len(df[0]))             >>2780
# print(len(df.iloc[:, 0]))     >>136


#UNIXコマンド
# $cut -f 1  popular-names.txt | sort | uniq
