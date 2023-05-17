n = int(input())

count = 0;

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)

'''
 if '3' == str(i) or '3' == str(j) or '3' == str(k)
 가 안된 이유
 문자열 자체로 봐야함

 3시 19분 35 초라면 이것도 카운트
 전체 문자열에서 3이 포함된걸 검사해야함
'''