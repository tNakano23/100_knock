import MeCab


# #ファイル実行開始時刻を取得

# #出力ファイル名
# out_file_name = "ochasen_" + timestr +  ".txt"
# with open(out_file_name, 'w') as f:
# 	f.write(text)

with open("4/neko.txt", encoding='utf-8') as f:
	text = f.read()
print(text)

# mecab = MeCab.Tagger("-Owakati")
# text = mecab.parse('解析文字列はこちらです。')
# mecab.parse('')