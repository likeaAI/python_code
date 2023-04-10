import tkinter as tk
import random

def item_enhancement(item_level, success_rate):
    enhancement_count = 0
    while True:
        if random.random() < success_rate:
            item_level += 1
            enhancement_count += 1
        else:
            return False, enhancement_count, success_rate

        if item_level == 15:
            return True, enhancement_count, success_rate

def enhance_item():
    global item_level, success_rate, result_label
    is_max_level, enhancement_count, success_rate = item_enhancement(item_level, success_rate)
    if is_max_level:
        result_label.config(text=f"아이템 강화를 성공적으로 마쳤습니다! 최종 아이템 레벨: {item_level}\n강화 성공 횟수: {enhancement_count}\n성공 확률: {success_rate*100:.1f}%")
        item_level = 0
        success_rate = 0.5
    else:
        result_label.config(text="아이템 강화를 실패하여 처음부터 다시 시작합니다.")
        item_level = 0
        success_rate = 0.5

def quit_game():
    window.destroy()

window = tk.Tk()
window.title("아이템 강화 게임")

item_level = 0
success_rate = 0.5

level_label = tk.Label(window, text=f"현재 아이템 레벨: {item_level}")
level_label.pack(pady=5)

rate_label = tk.Label(window, text=f"강화 확률: {success_rate*100:.1f}%")
rate_label.pack(pady=5)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

enhance_button = tk.Button(window, text="아이템 강화", command=enhance_item)
enhance_button.pack(pady=5)

quit_button = tk.Button(window, text="종료", command=quit_game)
quit_button.pack(pady=5)

window.mainloop()
