import sys
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, fromstring, tostring, XML
from xml.dom import minidom
from lxml import etree
import glob
import time
import requests

"""
実行dir: pepper/objectdetection
目的: xmlファイルのpathを変更する
"""

# ディレクトリ内のファイル取得
CURRENT_DIR = os.getcwd()
print(CURRENT_DIR)
print('変更開始')
XML_DIR = os.path.join(CURRENT_DIR, 'annotations', 'xmls')
IMG_DIR = os.path.join(CURRENT_DIR, 'images')
files = glob.glob(XML_DIR+"/*.xml")

# xmlファイルの修正
for i in range(len(files)):
	try:
		file_name = files[i].split("/")[-1].split('.')[0]
		file_DIR = os.path.join(IMG_DIR, file_name)
		print(file_DIR)

		# ファイルをチェックする
		tree = ET.parse(files[i])
		root = tree.getroot()
		"""folderタグを書き直す"""
		# folder_text = tree.find('folder')
		# folder_text.text = "images"
		"""２つ目のannotationタグ、imageタグを消去"""
		# for e in root:
		# 	for c1 in e:
		# 		if c1.tag == 'image' or c1.tag == 'annotation':
		# 			e.remove(c1)
		# 		for c2 in c1:
		# 			if c2.tag == 'image':
		# 				c1.remove(c2)

		"""pathタグがあるかチェック"""
		check = False #pathがない
		for e in root:
			if e.tag == 'path':
				check = True
				# 上書き
				path_text = root.find('path')
				path_text.text = file_DIR+".jpg"
				break
			else:
				pass
		if check == False:
			# 追加するタグの作成
			children = XML("<path>"+file_DIR+".jpg</path>")
			root.append(children)

		tree.write(files[i], 'utf-8', True)

	except:
		print("error: "+files[i])
		time.sleep(10)
