from watchdog.observers import Observer
from watchdog.events import *
import time
import os

"""
监测文件夹、文件是否有变化
"""

class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)
    
    def chkfile(self, info):
        tm = time.localtime(time.time())
        datetime = str(tm[0]) + str(tm[1]) + str(tm[2])
        logpsth = 'G:\\黄大宝python\\测试目录\\log'
        checkName = os.path.join(logpsth,"ChangeFileNames{0}".format(datetime) + ".txt")
        
        if not os.path.isfile(checkName):
            fs = open(checkName, 'w+')
            fs.close()
            print("OK????")
        return checkName
    
    def WriteInfo(self, filename, info):
        with open(filename, 'r+') as fs:
            fs.readlines()
            fs.write('\n')
            fs.write(info)
            fs.write('\n')
            
    def on_moved(self, event):
        if event.is_directory:
            print("directory moved from {0} to {1}".format(event.src_path, event.dest_path))
        else:
            print("file moved from {0} to {1}".format(event.src_path, event.dest_path))

    def on_created(self, event):
        if event.is_directory:
            print("directory created:{0}".format(event.src_path))
        else:
            print("file created:{0}".format(event.src_path))

    def on_deleted(self, event):
        if event.is_directory:
            print("directory deleted:{0}".format(event.src_path))
        else:
            print("file deleted:{0}".format(event.src_path))

    def on_modified(self, event):
        info = event.src_path
        print("file modified:{0}".format(info))
        filename = self.chkfile(info)
        self.WriteInfo(filename, info)
        # print("file modified:{0}".format(event.src_path))
        # if event.is_directory:
        #     print("directory modified:{0}".format(event.src_path))
        # else:
        #     print("file modified:{0}".format(event.src_path))
        

if __name__ == "__main__":
    dpath = "G:\\黄大宝python\\测试目录\\testDirs"
    observer = Observer()
    event_handler = FileEventHandler()
    observer.schedule(event_handler, dpath, True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()