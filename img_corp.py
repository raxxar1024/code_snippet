# -*- coding: utf-8 -*-  
from PIL import Image
import os
import os.path


IMAGE_X1 = 75
IMAGE_Y1 = 75
IMAGE_X2 = 1575
IMAGE_Y2 = 1200
ROOT_DIR = "ori/"
BACK_DIR = "corp/"


def corp(img_path, bak_path):
    # 打开图片句柄
    im = Image.open(img_path)

    # 设定裁剪区域
    box = (IMAGE_X1, IMAGE_Y1, IMAGE_X2, IMAGE_Y2)

    # 裁剪图片，并获取句柄region
    region = im.crop(box)

    # 保存图片
    region.save(bak_path)


def traversal_file(dir_path):
    path_dirs = os.listdir(dir_path)
    for file_dir in path_dirs:
        child = os.path.join('%s%s' % (dir_path, file_dir))
        img_path = child.decode('gbk')
        child_bak = os.path.join('%s%s' % (BACK_DIR, file_dir))
        bak_path = child_bak.decode('gbk')
        corp(img_path, bak_path)

if __name__ == "__main__":
    traversal_file(ROOT_DIR)
