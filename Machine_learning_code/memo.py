# enumerate : 인덱스를 달아줌
#zip : 두개를 병렬적으로 출력
#lambda : 이름없는 익명함수
#for i in map(ex) 처럼 list없이 쓸수 있다.
#print(list(map(f,ex))) ex라는 시퀀스에 f라는 함수 적
#파이선3에서는 map앞에 list를 붙여주어야 한다.
#from functools import reduce
#print(reduce(lambda x,y : x+y, [1,2,3,4,5]))
#계속 누적되어 계산 위의 결과값 15

# 팩토리얼 reduce
#def factorial(n):
#        return reduce(
#         lambda x, y: x*y, range(1, n+1))

# *(asterisk) 한번에 여러개의 변수를 받음
# **이면 변수명도 다 지정됨
# 함수사용할때 *붙여야 unpacking됨
#data = {"b":1, "c":2,"d":3}
#aster(10,*data)
#[] - >리스트 ()->튜플 {}-> 딕트  모두 벡터

#matrix_a = [[1, 1, 2], [2, 1, 1]]
#matrix_b = [[1, 1], [2, 1], [1, 3]]
#result = [[sum(a * b for a, b in zip(row_a, column_b))
          #for column_b in zip(*matrix_b)] for row_a in matrix_a]
#print(result)

# set -> unique한 값을 가지는 집합셋
conda create -n ml_scratch python=3.6 # 가상환경생성
activate ml_scratch # 가상환경실행
conda install pandas
