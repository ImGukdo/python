import numpy as np

# 배열 합치기
a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])
a3 = np.concatenate([a1, a2])
print(a3)  # [1 2 3 4 5 6]

# 2차원배열 합치기
# 세로로 합치기
a4 = np.arange(4).reshape(1, 4)
a5 = np.arange(4, 12).reshape(2, 4)
a6 = np.concatenate([a4, a5])
print(a6)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
a7 = np.vstack([a4, a5])
print(a7)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# 가로로 합치기
a8 = np.arange(4).reshape(2, 2)
a9 = np.arange(4, 8).reshape(2, 2)
a10 = np.concatenate([a8, a9], axis = 1)
print(a10)
# [[0 1 4 5]
#  [2 3 6 7]]
a11 = np.hstack([a8, a9])
print(a11)
# [[0 1 4 5]
#  [2 3 6 7]]

# 배열 나누기
# 가로로 나누기
a12 = np.arange(8).reshape(2, 4)
left, right = np.split(a12, [2], axis = 1)  # 가로축 인덱스2를 기준으로 왼쪽과 오른쪽으로 나눈다.
print(left)
# [[0 1 4 5]
#  [2 3 6 7]]
print(right)
# [[0 1 4 5]
#  [2 3 6 7]]

#세로로 나누기
up, down = np.split(a12, [1], axis = 0)  # 세로축 인덱스1을 기준으로 위와 아래로 나눈다.
print(up)  # [[0 1 2 3]]
print(down)  # [[4 5 6 7]]
