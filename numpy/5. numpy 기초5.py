import numpy as np

# 논리 연산
a1 = np.array([1, 2, 3, 4])
a2 = np.array([4, 2, 2, 4])
print(a1 == a2)  # [False  True False  True]
print(a1 >= a2)  # [False  True  True  True]
print(np.all(a1 == a2))  # False 모든 요소가 조건을 만족해야 True

# np.logical_and() : and 연산함수
# np.logical_or() : or 연산함수
print(np.logical_and(a1 > 2, a1 < 5))  # [False False  True  True]
print(np.logical_or(a2 >3, a2 < 4))  # [ True  True  True  True]

# np.where(조건, 참일때 실행, 거짓일때 실행)
print(np.where(a1 < 3, -1, 100))  # [ -1  -1 100 100]

# 배열을 1차원으로 변경, np.ravel(), np.flatten()
a3 =  np.arange(12).reshape(3, 4)
print(a3)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
print(a3.ravel())  # [ 0  1  2  3  4  5  6  7  8  9 10 11]
print(a3.flatten())  # [ 0  1  2  3  4  5  6  7  8  9 10 11]

#  numpy 원소 오름차순 정렬
a4 = np.array([7, 45, 21, 33, 1])
a4.sort()
print(a4)  # [ 1  7 21 33 45]

# 내림차순 정렬
print(a4[::-1])  # [45 33 21  7  1]

# 세로축을 기준으로 정렬하기
a5 = np.array([[9, 1, 20, 14], [11, 10, 7, 13]])
a5.sort(axis = 0)
print(a5)
# [[ 9  1  7 13]
#  [11 10 20 14]]

# numpy 배열 객체 복사
a6 = np.arange(5)  # [0  1  2  3  4]
a7 = a6
a7[0] = 10
print(a6)  # [10  1  2  3  4]

a7 = a6.copy()
a7[0] = 99
print(a6)  # [10  1  2  3  4]

# 중복된 원소 제거
a8 = np.array([1, 1, 1, 2, 3, 3, 4, 5, 5, 3, 4])
a9 = np.unique(a8)
print(a9)  # [1 2 3 4 5]

# 단일 객체 저장 및 불러오기
a10 = np.arange(10)
np.save("saved.npy", a10)

a11 = np.load("saved.npy")
print(a11)  # [0 1 2 3 4 5 6 7 8 9]

# 복수 객체 저장 및 불러오기
a12 = np.arange(5)
a13 = np.arange(5, 10)
np.savez("saved2.npz", array1 = a12, array2 = a13)
data = np.load("saved2.npz")
print(data["array1"])  # [0 1 2 3 4]
print(data["array2"])  # [5 6 7 8 9]