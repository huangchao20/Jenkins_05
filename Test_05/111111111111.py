import sys
import time

print(dir(sys))

def PrintInfo(total):
    for i in range(total):
        if i + 1 == total:
            percent = 100.0
            print('当前核算进度 : %s [%d/%d]' % (str(percent) + '%', i + 1, total), end='\n')
        else:
            percent = round(1.0 * i / total * 100, 2)
            print('当前核算进度 : %s [%d/%d]' % (str(percent) + '%', i + 1, total), end='\r')
        # time.sleep(0.01)

if __name__ == '__main__':
    total = 153000000
    PrintInfo(total)