'''
  제작자 : 실습조교 컴퓨터교육과 강준우

  프로그램 설명 : 
    전체 과제를 다운받아도, 이 프로그램을 쓰면
    우리 분반 학생들의 과제만 남겨줍니다.

  사용법 : 
    1. 디렉토리 하나에 다음을 준비해줍니다.
      - 전체 학생들의 과제
      - 학생들 이름이 담긴 txt파일(줄바꿈으로 구분되어야 합니다.)
      - 지금 이 파이썬 파일

    2. 터미널을 열고 해당 디렉토리로 이동후,
      >>python only_our_students.py "txt파일이름"
      으로 실행해주면, txt에 있는 이름 빼고 다 삭제해줍니다.

  주의사항 : 
    이름이 두글자일때와 세글자일때만 고려했습니다.
    4글자 이상의 이름을 가진 학생은, 첫 3글자가 같으면 있는 것으로 여겨집니다.
    따라서 대부분 정확하겠지만, 100% 정확성을 보장하진 않습니다.

  즐거운 채점 되세요.
'''

import os, sys

def main(our_students_txt):
  #현재 디렉토리에서 과제명들을 추출합니다.
  homeworks=os.listdir()
  del homeworks[homeworks.index(our_students_txt)]
  del homeworks[homeworks.index('only_our_students.py')]

  #txt 파일에서 학생 이름들을 추출합니다.
  with open(our_students_txt, 'r', encoding='utf-8') as f:
    students=[student.rstrip() for student in f]

  #만약 학생이 학생리스트에 없을 경우, 과제파일을 삭제합니다.
  for hwname in homeworks:
    if not (hwname[:3] in students or (hwname[:2] in students and hwname[2]=='2')):
      print(f'removing {hwname}')
      os.remove(hwname)
  
  print('complete')

if __name__ == "__main__":
  main(sys.argv[1])