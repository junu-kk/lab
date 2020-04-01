import os, sys
from time import sleep

def exit_process(msg):
  print(msg)
  sleep(3)
  exit()

def main():
  #일단 외자와 동명이인은 고려하지 않겠습니다.
  HW_PATH="C:/Users/brian/Documents/june/Univ/3-1/(조교)자료구조/3-C언어의기본자료형활용"
  hw_dirs=os.listdir(HW_PATH)
  for hw_dir in hw_dirs:
    os.rename(HW_PATH+'/'+hw_dir,HW_PATH+'/'+hw_dir[:3])
  

  

main()