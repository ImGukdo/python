import numpy as np
# 배열이란 순서가 있는 '같은 종류'의 데이터가 저장된 집합

# 리스트로부터 1차원 배열을 생성
data1 = [0, 1, 2, 3, 4, 5]
a1 = np.array(data1)
print(a1)  # [0 1 2 3 4 5]

# 리스트 데이터를 직접 넣어서 배열 객체를 생성
a2 = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
print(a2)  # [0.1 0.2 0.3 0.4 0.5]

# 범위를 지정해 배열 생성
a3 = np.arange(0, 6)  # arange([start,] stop [, step])
print(a3)  # [0 1 2 3 4 5]

# 다차원 배열 생성
a4 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a4)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# 배열의 형태 변환
a5 = np.arange(0, 12)
print(a5)  # [ 0  1  2  3  4  5  6  7  8  9 10 11]
a6 = a5.reshape(3, 4)
print(a6)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# 시작과 끝을 지정하고 데이터의 개수를 지정해 배열생성
a7 = np.linspace(0, 10, 7)  # linspace([start, stop [, num]) num default값은 50
print(a7)  # [ 0.          1.66666667  3.33333333  5.          6.66666667  8.33333333  10.        ]

# 배열 객체의 타입을 확인
print(a1.dtype)  # int32
print(a2.dtype)  # float64
# 배열의 형태를 확인
print(a6.shape)  # (3, 4)
# 배열의 크기를 확인
print(a4.size)  # 9
print(a5.size)  # 12
print(a6.size)  # 12
