import random

def number_guessing_game():
    # 1에서 100 사이의 숫자를 무작위로 선택
    target_number = random.randint(1, 100)
    attempts = 0

    print("1에서 100 사이의 숫자를 맞춰보세요!")

    while True:
        #숫자 입력 받기
        guess = int(input("숫자를 입력하세요: "))
        attempts += 1

        # 입력한 숫자가 정답인 경우
        if guess == target_number:
            print(f"축하합니다! 시도횟수:{attempts} 정답은 {target_number}입니다.")
            break
        # 입력한 숫자가 더 큰 경우
        elif guess > target_number:
            print("높음")
        # 입력한 숫자가 더 작은 경우
        else:
            print("낮음")

# 게임 시작
number_guessing_game()
