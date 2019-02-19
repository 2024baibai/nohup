#-*- coding=utf-8 -*-
import subprocess
import threading
import time

def run():
    cmd='nohup python child.py &'
    subprocess.Popen(cmd,shell=True)


def main():
    t=threading.Thread(target=run)
    t.start()
    for i in range(100):
        time.sleep(1)

if __name__=='__main__':
    main()
