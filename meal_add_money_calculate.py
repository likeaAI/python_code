import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
import pickle
import sys

shift_pattern = ["오전"] * 5 + ["휴무"] + ["야간"] * 5 + ["휴무"] * 2 + ["오후"] * 5 + ["휴무"] * 2

def is_holiday(date):
    # For simplicity, consider Saturday and Sunday as holidays
    return date.weekday() == 5 or date.weekday() == 6

def calculate_pattern_start_date(shift_pattern, reference_date, shift_type, shift_day):
    pattern_length = len(shift_pattern)
    shift_index = shift_pattern.index(shift_type)
    pattern_start_date = reference_date - timedelta(days=(shift_index + shift_day - 1))
    if pattern_start_date > reference_date:
        pattern_start_date -= timedelta(days=pattern_length)
    return pattern_start_date

def show_shift_and_meal_info():
    reference_date = datetime.strptime(reference_date_entry.get(), "%Y-%m-%d")
    shift_type, shift_day = shift_info_entry.get().split()
    shift_day = int(shift_day)
    start_date = datetime.strptime(start_date_entry.get(), "%Y-%m-%d")
    end_date = datetime.strptime(end_date_entry.get(), "%Y-%m-%d")
    morning_holiday_count = int(morning_holiday_count_entry.get())

    pattern_start_date = calculate_pattern_start_date(shift_pattern, reference_date, shift_type, shift_day)

    meal_allowance = 0
    schedule = ""
    current_date = start_date
    pattern_length = len(shift_pattern)
    while current_date <= end_date:
        shift_type_today = shift_pattern[(current_date - pattern_start_date).days % pattern_length]
        
        if shift_type_today == "오전" and is_holiday(current_date):
            schedule += f"{current_date.strftime('%Y-%m-%d (%A)')}: {shift_type_today} (식비지급)\n"
            meal_allowance += 8000
        elif shift_type_today not in ["오전", "휴무"]:
            schedule += f"{current_date.strftime('%Y-%m-%d (%A)')}: {shift_type_today} (식비지급)\n"
            meal_allowance += 8000
        else:
            schedule += f"{current_date.strftime('%Y-%m-%d (%A)')}: {shift_type_today}\n"
        
        current_date += timedelta(days=1)

    meal_allowance += morning_holiday_count * 8000
    schedule += f"\n식비 지급 횟수: {meal_allowance // 8000}회\n총 식비: {meal_allowance}원"

    messagebox.showinfo("근무 일정 및 식비 정보", schedule)

def save_last_input():
    last_input = {
        "reference_date": reference_date_entry.get(),
        "shift_info": shift_info_entry.get(),
        "start_date": start_date_entry.get(),
        "end_date": end_date_entry.get(),
        "morning_holiday_count": morning_holiday_count_entry.get(),
    }
    with open("last_input.pkl", "wb") as f:
        pickle.dump(last_input, f)

def load_last_input():
    try:
        with open("last_input.pkl", "rb") as f:
            last_input = pickle.load(f)
    except FileNotFoundError:
        return

    reference_date_entry.insert(0, last_input["reference_date"])
    shift_info_entry.insert(0, last_input["shift_info"])
    start_date_entry.insert(0, last_input["start_date"])
    end_date_entry.insert(0, last_input["end_date"])
    morning_holiday_count_entry.insert(0, last_input["morning_holiday_count"])

root = tk.Tk()
root.title("식대계산 및 근무표확인")

tk.Label(root, text="참조 날짜 (YYYY-MM-DD)").pack()
reference_date_entry = tk.Entry(root)
reference_date_entry.pack()

tk.Label(root, text="근무 패턴 정보 (근무 유형 공백 일수)").pack()
shift_info_entry = tk.Entry(root)
shift_info_entry.pack()

tk.Label(root, text="근무 시작 날짜 (YYYY-MM-DD)").pack()
start_date_entry = tk.Entry(root)
start_date_entry.pack()

tk.Label(root, text="근무 종료 날짜 (YYYY-MM-DD)").pack()
end_date_entry = tk.Entry(root)
end_date_entry.pack()

tk.Label(root, text="오전 공휴일 수").pack()
morning_holiday_count_entry = tk.Entry(root)
morning_holiday_count_entry.pack()

show_schedule_button = tk.Button(root, text="근무 일정 및 식비 정보 확인", command=show_shift_and_meal_info)
show_schedule_button.pack()

# 프로그램이 시작될 때 마지막 입력 값을 불러옴
exit_button = tk.Button(root, text="종료", command=sys.exit)
exit_button.pack()

root.protocol("WM_DELETE_WINDOW", lambda: (save_last_input(), sys.exit(0)))  # sys.exit(0) 추가  # 프로그램이 종료될 때 마지막 입력 값을 저장
load_last_input()  # 프로그램이 시작될 때 마지막 입력 값을 불러옴

root.mainloop()
