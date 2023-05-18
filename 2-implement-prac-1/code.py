location = input()

row = str(location[0])
column = int(location[1])

alpha = ["a", "b", "c", "d", "e", "f", "g", "h"]

find_alpha = int(alpha.index(row)) + 1 # row 를 숫자로 변환

night = [find_alpha, column] # 나이트의 위치를 저장

array = [
    [-1, -2], # "upleft"
    [1, -2], # "upright"
    [-2, -1], # "leftup"
    [-1, 1], # "leftdown"
    [-1, 2], # "downleft"
    [1, 2], # "downright"
    [2, -1], # "rightup"
    [2, 1] # "rightdown"
]

count = 0

for i in array:
    nx = night[0] + i[0]
    ny = night[1] + i[1]
    if 0 < nx <= 8 and 0 < ny <= 8:
        count += 1
print(count)