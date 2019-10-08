import os

class Package:
    def __init__(self, dpath):
        self.dpath = dpath
        
    def checkSql(self):
        print("这逼玩意儿胎神")
    
    def checkCfg(self):
        print("是那个胎神嘛")
    
    def checkFileNames(self):
        print("就是那个卅")
    
    def PackCodes(self):
        print("二傻子")
    
    def QuitOut(self):
        print("你给我滚吧!!")
        return -1
        
    def main(self):
        print("###########################################################################")
        print("##########输入要执行的操作：     ")
        print("##########输入1：检查sql文件是否满足提版要求")
        print("##########输入2：检查配置文件")
        print("##########输入3：检查脚本命名是否规范")
        print("##########输入4：代码打包")
        print("##########输入e：退出程序")
        print("###########################################################################")
        while True:
            flag = input(">>>>>>:")
            print("Ready Go!~~")
            if flag == "1":
                self.checkSql()
            elif flag == "2":
                self.checkCfg()
            elif flag == "3":
                self.checkFileNames()
            elif flag == "4":
                self.PackCodes()
            elif flag == "e":
                answerBox = input(">>>>>是否确认退出:Y/N")
                if answerBox == "y" or answerBox.upper() == "Y":
                    ret = self.QuitOut()
                    if ret == -1:
                        break
                else:
                    self.main()
            else:
                print("你他妈的都输入的啥子？？？~~~")
if __name__ == '__main__':
    dpath = "123"
    pack = Package(dpath)
    pack.main()