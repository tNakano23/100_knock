import pandas as pd
def file_spiter(path, split_step):
    df = pd.read_table("2/popular-names.txt", header=None)
    idx = df.shape[0] // split_step
    for i in range(split_step):
        df_split = df.iloc[i * idx : (i + 1) * idx]
        df_split.to_csv(f"popular-names{i}.txt", sep="\t",header=False, index=False)

file_spiter("2/popular-names.txt", 6)


#UNIXコマンド
# $split -l 6 popular-names.txt 




"""
split_step = 6
idx = df.shape[0] // split_step       #463

print(i * idx ,":", (i + 1) * idx)
  >>>
  0 : 463
  463 : 926
  926 : 1389
  1389 : 1852
  1852 : 2315
  2315 : 2778
"""