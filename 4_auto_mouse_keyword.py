import tkinter as tk
import pyautogui


# 마우스 커서 이동 함수
def move_mouse():
    # 마우스 커서 좌표 가져오기
    x, y = pyautogui.position()

    # 마우스 커서 이동
    pyautogui.moveTo(x + 10, y + 10, duration=0.25)


# 대상 단어
target_word = "마우스"

# GUI 생성
root = tk.Tk()
root.title("특정 단어 감지")


# 시작 버튼 클릭시 실행
def start():
    # 반복하여 검사
    while True:
        # 화면 캡처
        screenshot = pyautogui.screenshot(region=None)

        # 대상 단어가 있는지 확인
        if target_word in screenshot:
            move_mouse()


# 시작 버튼 생성
start_button = tk.Button(root, text="시작", command=start)
start_button.pack(pady=10)

# 종료 버튼 생성
exit_button = tk.Button(root, text="종료", command=root.quit)
exit_button.pack()

# GUI 실행
root.mainloop()

