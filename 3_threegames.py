import tkinter as tk
import random

# 게임 승리 조건 설정
WIN_CONDITION = 3

def play_game(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(["가위", "바위", "보"])
    result = ""

    if user_choice == computer_choice:
        result = "무승부"
    elif (user_choice == "가위" and computer_choice == "보") or (user_choice == "바위" and computer_choice == "가위") or (user_choice == "보" and computer_choice == "바위"):
        result = "이겼습니다!"
        user_score += 1
    else:
        result = "졌습니다..."
        computer_score += 1

    result_label.config(text=f"컴퓨터: {computer_choice}, 결과: {result}")

    # 세 번 이상 이긴 경우 게임 종료
    if user_score >= WIN_CONDITION:
        result_label.config(text=f"게임 종료! 사용자 승리!")
        disable_buttons()
    elif computer_score >= WIN_CONDITION:
        result_label.config(text=f"게임 종료! 컴퓨터 승리!")
        disable_buttons()

def disable_buttons():
    rock_button.config(state=tk.DISABLED)
    scissor_button.config(state=tk.DISABLED)
    paper_button.config(state=tk.DISABLED)

def quit_game():
    window.destroy()

window = tk.Tk()
window.title("가위바위보 게임")

user_score = 0
computer_score = 0

rock_button = tk.Button(window, text="바위", width=10, height=5, command=lambda: play_game("바위"))
rock_button.pack(side=tk.LEFT, padx=10, pady=10)

scissor_button = tk.Button(window, text="가위", width=10, height=5, command=lambda: play_game("가위"))
scissor_button.pack(side=tk.LEFT, padx=10, pady=10)

paper_button = tk.Button(window, text="보", width=10, height=5, command=lambda: play_game("보"))
paper_button.pack(side=tk.LEFT, padx=10, pady=10)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

quit_button = tk.Button(window, text="종료", command=quit_game)
quit_button.pack(side=tk.BOTTOM, pady=10)

window.mainloop()
