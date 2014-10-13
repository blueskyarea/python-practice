# coding: UTF-8
# うるう年の判定

import sys
# 引数取得
args = sys.argv
argc = len(args)
# 引数チェック
if (argc == 1):
    print("引数が指定されていません")
    quit()
if (args[1].isdigit() == False):
    print("引数が数字ではありません")
    quit()

# うるう年の判定
year = int(args[1])
if (year % 4 == 0):
    print(args[1] + "年はうるう年です")
else:
    print(args[1] + "年はうるう年ではありません")
