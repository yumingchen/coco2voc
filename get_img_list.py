import os.path as osp
import cv2
import numpy as np
import glob
import argparse
def get_img_list(args, target='train'):
       
    root_dir = args.root_dir
    xml_path = osp.join(root_dir, 'Annotations/', 'COCO_{}2014**.xml'.format(target))
    print(xml_path)
    xml_list = glob.glob(xml_path)
    img_list = []
    for line in xml_list:
        line = line.split('/')[-1].split('.')[0]
        img_list.append(line+'\n')
    print(len(img_list))
    print(img_list[:10])
    with open(osp.join(root_dir, 'ImageSets/Main/', target+'.txt'), 'w') as f:
        f.writelines(img_list)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--root_dir', default='/home/cym/CYM/dataset/VOC_COCO_persons/voc_coco_persons/',
                       type=str, help='root path')
#     parser.add_argument('--target' default='trian', type=str, help='train.txt or val.txt', choices=['train', 'val'])
    args = parser.parse_args()
    get_img_list(args, target='train')
    get_img_list(args, target='val')