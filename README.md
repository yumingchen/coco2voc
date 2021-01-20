# coco2voc
* Convert coco2014 Json Annotations to PASCAL VOC Format

### requirement
* python3.6
* numpy
* xml
* json
* cytools

### How to Run
* 将COCO80个类全部转换成VOC格式
```
python coco3voc.py --anno_file /home/cym/CYM/dataset/COCO2014/coco/annotations/instances_train2014.json --output_dir /home/cym/CYM/dataset/COCO_voc/
```
* 只转换某一类，如person
```
python coco3voc.py --anno_file /home/cym/CYM/dataset/COCO2014/coco/annotations/instances_train2014.json --output_dir /home/cym/CYM/dataset/COCO_voc/ --target_cls person
```
> > * --anno_file: coco的标注文件, eg.[instances_train2014.json instances_val2014].
> > * --output_dir: 保存voc格式的xml文件。
> > * --target_cls: 想要转换的类别.
* 获取img_list [trian.txt, val.txt]
```
python get_img_list.py --root_dir /home/cym/CYM/dataset/VOC_COCO_persons/voc_coco_persons/
```
> > * --root_dir: 表示上述生成的xml所在路径.想要将xml文件放到Annotations文件夹下。





