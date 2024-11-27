def sum_of_odds(n):
    # 홀수들의 합을 저장할 변수를 초기화 시킨다
    odd_sum = 0
    
    # 1부터 N까지의 수를 반복하면서 홀수인지 확인하고 합산
    for i in range(1, n + 1):
        if i % 2 != 0:
            odd_sum += i
    
    return odd_sum

# 정수 입력 
N = int(input("정수 N을 입력하세요: "))
result = sum_of_odds(N)

#출력
print(f"1부터 {N}까지의 홀수들의 합은 {result}입니다.")

