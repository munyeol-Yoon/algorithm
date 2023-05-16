n, m, k = map(int, input().split())
print(n, m, k)
# k 는 한 숫자가 더해질수 있는 횟수, m 은 연산 횟수, n 은 배열의 크기
data = list(map(int, input().split()))
print(data)

result = 0
# 결과를 저장

data.sort()
# 입력한 데이터 정렬

big = data[len(data) - 1]
# 가장 큰 값
littleBig = data[len(data) - 2]
# 두 번째로 큰 값
print(big)
print(littleBig)

end_loop = 0
# 루프를 끝내기 위한 변수 end_loop
while end_loop != 1:
    # end_loop 가 1이 되면 종료된다.
    for i in range(k):
        # 한 숫자가 더해질수 있는 횟수인 k 변수 만큼 for 루프가 반복된다
        if m <= 0:
            # 연산횟수인 m 이 0 과 같아지거나 적어지면 종료된다.
            end_loop = 1
            break
        # 가장 큰값인 big 변수를 result 에 더해준다.
        result += big
        print("result1:",result)
        # 연산횟수인 m 변수를 1 빼준다.
        m -= 1
        print("m:",m)
    
    if m <= 0:
        end_loop = 1
        break
    # 두번째로 큰값인 littleBig 변수를 result 에 더해준다.
    result += littleBig
    print("result2:",result)
    # 연산횟수인 m 변수를 1 빼준다.
    m -= 1
    print("m2:",m)

print(result)
