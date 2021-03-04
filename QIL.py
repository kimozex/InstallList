#-*- coding:utf-8 -*-
import subprocess
import sys

# traverse the software list
output= subprocess.check_output(['wmic', 'product', 'get', 'name'])
data = output.decode("cp949")
lines = data.splitlines()


for i in lines:
    print(i)