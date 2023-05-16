n, k = map(int, input().split())

result = 0

while n >= k:
    # n 이 k 랑 같거나 n이 더 클때까지 반복
    while n % k != 0:
        # n 과 k 를 나누었을때 0 이 아니면 계속 반복
        n -= 1
        result += 1
    n //= k
    result += 1

while n > 1:
    # 남은 수 1씩빼기
    n -= 1
    result += 1

print(result)
