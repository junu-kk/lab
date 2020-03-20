'''
#### 제작자 : 실습조교 컴퓨터교육과 강준우

#### 프로그램 설명 :
전체 과제를 다운받아도, 이 프로그램을 쓰면 우리 분반 학생들의 과제만 남겨줍니다.

#### 사용법 :
1. 디렉토리 하나에 다음을 준비해줍니다.
  * 전체 학생들의 과제(압축은 풀린 상태여야겠죠?)
  * 학생들 이름이 담긴 txt파일 : 학생이름이 줄바꿈으로 구분되어야 하고, txt파일 이름은 자유입니다.
  * 지금 이 파이썬 파일

2. only_our_students.py를 더블클릭해 실행하시면 됩니다.

#### 주의사항 :
이름이 두글자일때와 세글자일때만 고려했습니다.
4글자 이상의 이름을 가진 학생은, 첫 3글자가 같으면 있는 것으로 여겨집니다.
따라서 대부분 정확하겠지만, 100% 정확성을 보장하진 않습니다.

즐거운 채점 되세요.
'''

import os, sys
from time import sleep

#msg를 띄우며 프로그램을 종료하는 함수입니다.
def exit_process(msg):
  print(msg)
  sleep(3)
  exit()

#디렉토리 내 txt파일 개수에 따라 처리해주는 함수입니다.
def process_txts(txts):
  if not txts:
    exit_process('txt 파일이 존재하지 않습니다.')
  elif len(txts)==1:
    YorN=input(f'학생 이름이 담긴 txt파일이 {txts[0]} 인가요? Y/N : ')
    if YorN=='Y' or YorN=='y':
      return txts[0]
    else:
      exit_process('올바른 학생 txt파일을 만들어주세요.')
  else:
    for i in range(len(txts)):
      print(f'{i+1}. {txts[i]}')
    choice=int(input('학생 이름이 담긴 txt 파일의 번호를 입력해주세요 : '))
    return txts[choice-1]

#메인함수입니다.
def main():
  homeworks=os.listdir()
  del homeworks[homeworks.index('only_our_students.py')]
  txts=[]
  for hw in homeworks:
    if hw[-4:]=='.txt':
      txts.append(hw)

  our_students_txt=process_txts(txts)
  del homeworks[homeworks.index(our_students_txt)]

  #txt 파일에서 학생 이름들을 추출합니다.
  with open(our_students_txt, 'r', encoding='utf-8') as f:
    students=[student.rstrip() for student in f]

  #만약 학생이 학생리스트에 없을 경우, 과제파일을 삭제합니다.
  for hwname in homeworks:
    if not (hwname[:3] in students or (hwname[:2] in students and hwname[2]=='2')):
      print(f'removing {hwname}')
      os.remove(hwname)
  
  exit_process('complete')

if __name__ == "__main__":
  main()