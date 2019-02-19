#-*- coding=utf-8 -*-
import time

for i in range(100):
    with open('test.txt','a') as f:
        f.write(str(i)+'\n')
    time.sleep(1)

