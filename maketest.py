# -*- coding: utf-8 -*-
import os

img_path = r"F:\\train\\helmet_detection\\test\\"
test_path = r"F:\\train\\helmet_detection\\testdata\\"


def file_name():
    """
     检测img_path test_path 存在差异的txt img文件
     创建 相差异的txt文件
    :return: null
    """
    jpg_list = []
    txt_list = []
    for root, dirs, files in os.walk(img_path):
        for file in files:
            print(os.path.splitext(file))
            if os.path.splitext(file)[1] == '.jpg':
                jpg_list.append(os.path.splitext(file)[0])
    for root, dirs, files in os.walk(test_path):
        for file in files:
            print(os.path.splitext(file))
            if os.path.splitext(file)[1] == '.txt':
                txt_list.append(os.path.splitext(file)[0])
    print(len(jpg_list))
    print(len(txt_list))
    diff = set(jpg_list).difference(set(txt_list))  # 差集，在a中但不在b中的元素
    # 差异文件名
    print(len(diff))
    print(diff)
    for txt_name in diff:
        f = open(os.getcwd() + os.sep + "testdata" + os.sep + txt_name + ".txt", encoding="utf-8", mode="a+")  # 打开文件
        f.close()
    # 其中os.path.splitext()函数将路径拆分为文件名+扩展名


if __name__ == '__main__':
    file_name()
