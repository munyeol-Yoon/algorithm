# 나의 코드

n = input()

move = list(map(str, input().split()))

its_me = [1, 1]

for i in move:
    if i == "R":
        its_me[1] += 1
    elif i == "L":
        its_me[1] -= 1
    elif i == "U":
        its_me[0] -= 1
    elif i == "D":
        its_me[0] += 1
    
    if its_me[0] == 0:
        its_me[0] += 1
    elif its_me[1] == 1:
        its_me[1] += 1
    
print(its_me[0], its_me[1])

'''
저자 코드

# N 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)

'''

'''
 === 두번째로 푼 코드 ===
n = int(input());

userLocation = [1,1]

# 방향에 대한 이동값을 딕셔너리 형태로 정의
dict = {
    # '방향' : [x, y]
    'L':[0, -1],
    'R':[0, 1],
    'U':[-1, 0],
    'D':[1, 0]
}

# list 형태로 가게될 방향을 입력 받는다.
move = list(map(str, input().split()))

for i in move:
    # nextX 에 유저의 x 와 딕셔너리의 x 를 더한다.
    nextX = userLocation[0] + dict[i][0]
    # nextY 에 유저의 y 와 딕셔너리의 y 를 더한다.
    nextY = userLocation[1] + dict[i][1]
    
    #nextX 가 0 이 아니면서 5와 같으면서 nextY 가 0 이 아니면서 5 와 같을때만
    #유저의 x와 y를 변경해준다.
    
    if 0 < nextX <= n and 0 < nextY <= n:
        userLocation = [nextX, nextY]

# 유저의 x, y 출력
print(userLocation[0], userLocation[1])
'''