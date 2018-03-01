# -*- coding: utf-8 -*-  
from PIL import Image
import os
import os.path


IMAGE_BORDER = 150

ROOT_DIR = "ori/"
BACK_DIR = "corp/"


def corp(img_path, bak_path):
    # 打开图片句柄
    im = Image.open(img_path)

    width = im.size[0]
    height = im.size[1]

    # 设定裁剪区域
    box = (IMAGE_BORDER, IMAGE_BORDER, width-IMAGE_BORDER, height-IMAGE_BORDER)

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
