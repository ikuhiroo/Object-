import cv2
import glob
import os
import re
from collections import defaultdict

"""
実行dir: pepper/objectdetection
"""
# ディレクトリ内のファイル取得
CURRENT_DIR = os.getcwd()
print(CURRENT_DIR)
IMG_DIR = os.path.join(CURRENT_DIR, 'images') #画像ファイル
ANT_DIR = os.path.join(CURRENT_DIR, 'annotations') #アノテーション関連
LM_DIR = os.path.join(CURRENT_DIR, 'label_map.pbtxt') #ラベル

# label情報からクラス名取得
with open(LM_DIR, "r", encoding="utf-8") as f:
  lines = f.readlines()

# 辞書（クラス名）
class_dict = {}
label = 1 #ラベル（１以上）
for line in lines:
    if line.find("name:") >= 0:
        class_dict[line[9:-2]] = label
        label += 1

files = glob.glob(IMG_DIR+"/*.jpg")
trainval = [] #書き込み用のリスト
label = 1 #ラベル（１以上）
for f in files:
    try:
        fname = os.path.splitext(os.path.basename(f))[0]
        fname_label = '_'.join(fname.split('_')[:-1])
        trainval.append(fname+" "+str(class_dict[fname_label]))
    except:
        pass
      
txt_file = os.path.join(ANT_DIR,"trainval.txt")
#save trainval.txt
with open(txt_file, "w", encoding="utf-8") as f:
  f.write("\n".join(trainval))
