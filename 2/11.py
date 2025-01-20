with open("2/popular-names.txt") as f :
    for data in f:
        data = data.replace("\n", "")
        print(data.replace("\t", " "))


#UNIXコマンド
# $sed 's/\t/ /g' 2/popular-names.txt
# （sed -i s/検索パターン/置換パターン ファイル名） *-iでファイルを上書き


