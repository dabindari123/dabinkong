def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# 리스트 초기화
numbers = []

#  5개의 숫자를 입력 받는다
print("5개의 숫자를 입력하세요:")
for _ in range(5):
    number = float(input())
    numbers.append(number)

# 평균값을 계산한다
average = calculate_average(numbers)

# 출력
print(f"입력한 숫자들의 평균은 {average}입니다.")

