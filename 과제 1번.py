def print_pyramid(N):
    for i in range(1, N + 1):
        # 공백을 앞에 추가한다
        for j in range(N - i):
            print(" ", end=" ")
        
        # 증가하는 부분
        for j in range(1, i + 1):
            print(j, end=" ")
        
        # 감소하는 부분
        for j in range(i - 1, 0, -1):
            print(j, end=" ")
        
        # 줄을 바꿀때
        print()

# 정수 입력받기
N = int(input("정수 N을 입력하세요: "))
print_pyramid(N)
