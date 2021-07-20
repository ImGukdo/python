import numpy as np

# numpy의 상수 연산
a1 = np.array([1, 2, 3, 4])  # [1 2 3 4]
a2 = a1 + 2
print(a2)  # [3 4 5 6]

a3 = a1 * 10
print(a3)  # [10 20 30 40]

# 서로 다른 형태의 numpy 연산, 브로드캐스트
a4 = np.arange(4).reshape(2, 2)
# [[0 1]
#  [2 3]]
a5 = np.array([10, 10])  # [10 10]
a6 = a4 + a5
print(a6)
# [[10 11]
#  [12 13]]

a7 = np.random.randint(0, 10, (4, 4))
print(a7)
# [[8 3 6 7]
#  [7 7 1 7]
#  [0 7 4 4]
#  [6 6 2 5]]
a8 = np.array([1, 2, 3, 4]).reshape(4, 1)  # [1 2 3 4]
a9 = a7 + a8
print(a9)
# [[ 9  4  7  8]
#  [ 9  9  3  9]
#  [ 3 10  7  7]
#  [10 10  6  9]]

# 배열의 인덱싱과 슬라이싱
a10 = np.arange(16).reshape(4, 4)
print(a10[2, 2])  # 10
a10[2, 2] = 100
print(a10)
# [[  0   1   2   3]
#  [  4   5   6   7]
#  [  8   9 100  11]
#  [ 12  13  14  15]]

print(a10[[0, 3], [0, 3]])  # [ 0 15]
a10[[0, 3], [0, 3]] = 99
print(a10)
# [[ 99   1   2   3]
#  [  4   5   6   7]
#  [  8   9 100  11]
#  [ 12  13  14  99]]

print(a10[2])  # [  8   9 100  11]
a10[2] = [50, 50, 50, 50]
print(a10)
# [[99  1  2  3]
#  [ 4  5  6  7]
#  [50 50 50 50]
#  [12 13 14 99]]

print(a10[1:3])
# [[ 4  5  6  7]
#  [50 50 50 50]]
a10[1:3] = 1
print(a10)
# [[99  1  2  3]
#  [ 1  1  1  1]
#  [ 1  1  1  1]
#  [12 13 14 99]]

print(a10[:, 2:4])
# [[ 2  3]
#  [ 1  1]
#  [ 1  1]
#  [14 99]]

print(a1)  # [1 2 3 4]
print(a1.shape)  # (4,)
a11 = a1[np.newaxis, :]  
print(a11)  # [[1 2 3 4]]
print(a11.shape)  # (1, 4)

# numpy의 마스킹 연산
a12 = np.arange(16).reshape(4, 4)
print(a12)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]
a13 = a12 < 10
print(a13)
# [[ True  True  True  True]
#  [ True  True  True  True]
#  [ True  True False False]
#  [False False False False]]
print(a12[a13])  # [0 1 2 3 4 5 6 7 8 9]
a12[a13] = 100
print(a12)
# [[100 100 100 100]
#  [100 100 100 100]
#  [100 100  10  11]
#  [ 12  13  14  15]]

# numpy의 집계 함수
a14 = np.arange(16).reshape(4, 4)
print("최대값 :", np.max(a14))  # 최대값 : 15
print("최소값 :", np.min(a14))  # 최소값 : 0
print("합계 :", np.sum(a14))  # 합계 : 120
print("평균 :", np.mean(a14))  # 평균 : 7.5
print("최대값 위치 :, np.argmax(a14))  # 최대값 위치 : 15
print("최소값 위치 :, np.argmin(a14))  # 최대값 위치 : 0

# 가로나 세로로 집계 합수 사용하기
print(np.sum(a14, axis = 0))  # 세로방향으로 합 구하기, [24 28 32 36]
print(np.sum(a14, axis = 1))  # 가로방향으로 합 구하기, [ 6 22 38 54]
print(np.argmax(a14, axis = 0))  # [3 3 3 3]
print(np.argmin(a14, axis = 1))  # [0 0 0 0]
      
