import os, sys
from time import sleep

def close_program(students, processed_students):
  s=set(students)
  ps=set(processed_students)
  no_hw_students=list(s-ps)
  if no_hw_students:
    for no_hw_student in no_hw_students:
      print(no_hw_student)
    exit_process('위 학생들은 과제를 제출하지 않았습니다.')
  else:
    exit_process('모든 학생들이 과제를 제출했습니다!')

#msg를 띄우며 프로그램을 종료하는 함수입니다.
def exit_process(msg):
  print(msg)
  print('엔터를 누르시면 프로그램을 종료합니다.')
  sys.stdin.readline()
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

  processed_students=[]
  #만약 학생이 학생리스트에 없을 경우, 과제파일을 삭제합니다.
  for hwname in homeworks:
    delete=True
    for student in students:
      #student와 hwname앞부분 일치할때 break
      if student==hwname[:len(student)]:
        delete=False
        processed_students.append(student)
        break
    
    if delete:
      print(f'removing {hwname}')
      os.remove(hwname)
  
  close_program(students, processed_students)

if __name__ == "__main__":
  main()