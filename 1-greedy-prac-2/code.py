n, m = map(int, input().split())
# n 변수와 m 변수를 입력받습니다.

result = 0

for i in range(n):
    # n 의 크기 만큼 루프를 반복합니다.
    arr = list(map(int, input().split()))  
    # n 만큼 값을 입력받는다.
    minNum = min(arr)
    # arr 중에 최소값을 minNum 변수에 넣습니다.
    result = max(minNum, result)
    # 큰 값을 result 에 저장합니다.
    
print(result)