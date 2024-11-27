import random

def roll_dice(num_rolls):
    # 주사위 빈도 수를 저장할 딕셔너리 초기화
    frequencies = {i: 0 for i in range(1, 7)}
    
    # 주사위를 num_rolls번 던지고 결과를 저장
    for _ in range(num_rolls):
        roll = random.randint(1, 6)
        frequencies[roll] += 1
    
    return frequencies

# 주사위를 1000번 던지기
num_rolls = 1000
frequencies = roll_dice(num_rolls)

# 결과 출력
print(f"주사위를 {num_rolls}번 던져 나온 값들의 빈도:")
for value, frequency in frequencies.items():
    print(f"{value}: {frequency}번")
