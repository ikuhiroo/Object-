# Object-Detection
## 手順書  
＜前処理＞  
・アノテーション付け  
・label_map.pbtxt   
・train_with_masks.record  
・val_with_masks.record  
・train_val.txt  
・configファイル  
＜学習＞  
＜評価＞  
・pbファイルの作成  
・jupyter notebookで評価  


## 前処理
### アノテーション付け、`labelImg`を立ち上げる  
[labelImgの参考URL](http://segafreder.hatenablog.com/entry/2016/11/27/101541)  
workdir : pepper/tools/labelImg  
`$ python labelImg`  

●GUIのコマンド  
>w → box  
cmd + s → 名前をつけて保存  
d → 次の画像へ

*** 
### label_map.pbtxtの作成  
workdir : /pepper/objectdetection  
outputdir : /pepper/objectdetection/label_map.pbtxt  
ex) item {id: 1, name: 'pug'}  

*** 
### train_with_masks.recordとval_with_masks.recordの作成  
workdir : /pepper/objectdetection   
outputdir : /pepper/objectdetection/  
`$ python create_tf_record.py`  
*** 
### Holdout法の分割の仕方をmainメソッド内で設定する
*** 
### train_val.txtの作成  
workdir : pepper/objectdetection  
outputdir : pepper/objectdetection/annotations/train_val.txt  
`$ python to_trainval.py`  
*** 
### train_val.txtの修正（パスの変更）
workdir : pepper/objectdetection  
outputdir : pepper/objectdetection/annotations/train_val.txt  
`$ python xmltag.py`  
*** 
### Object Detection Pipelineのconfigの設定  
#### model部  
・クラス数  
・利用するアルゴリズム（検出部分と認識部分）の設定  
・ハイパーパラメータ設定  
*** 
#### train_config部  
・バッチサイズ  
・最適化手法の設定とハイパーパラメータ設定  
・学習済みモデルの設定  
・エポック数  
*** 
#### train_input_reader部  
・train_with_masks.recordの保存場所  
・label_map.pbtxtの保存場所  
*** 
#### eval_config部  
・サンプル数  
eval_input_reader部  
・eval_with_masks.recordの保存場所   
・label_map.pbtxtの保存場所  

## 学習  
workdir : models-master/research  
outputdir : train_dir  
`$ python object_detection/train.py   
--logtostderr   
--pipeline_config_path=・・・/config  
--train_dir=・・・/train  `

## 評価  
### tensorboardを表示  
`$ tensorboard --logdir=・・・/train`  
*** 
### pdファイルの作成  
workdir : models-master/research  
outputdir : output_directory/frozen_inference_graph.pb  
`$ python object_detection/export_inference_graph.py 
--input_type=image_tensor   
--pipeline_config_path=・・・/config   
--trained_checkpoint_prefix=・・・/model.ckpt-x  
--output_directory=・・・/train`  
*** 
### jupyter notebookで評価  
>PATH_TO_CKPT = '・・・/frozen_inference_graph.pb'  
PATH_TO_LABELS = '・・・/label_map.pbtxt'  
NUM_CLASSES =   
