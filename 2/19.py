import pandas as pd
df = pd.read_table("2/popular-names.txt", header=None)
sr = df[0]
print(sr.value_counts())

#UNIXコマンド
# $cut -f 1  popular-names.txt | sort | uniq -c | sort -n -r