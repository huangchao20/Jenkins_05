import os
import functools
from shutil import copyfile

class packageCodes:
    def __init__(self, dpath):
        self.dpath = dpath

    def __Mkdir(self, dir):
        print("开始创建目录!!!")
        if not os.path.isdir(dir):
            os.mkdir(dir)
        else:
            print("目录已存在，不做任何修改")
    