import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
import pickle

# 교대근무 패턴
shift_pattern = ["오전"]*5 + ["휴무"] + ["야간"]*5 + ["휴무"]*2 + ["오후"]*5 + ["휴무"]*2

# 날짜 차이 계산
def calculate_pattern_start_date(shift_pattern, reference_date, shift_type, shift_day):
    pattern_length = len(shift_pattern)
    shift_index = (shift_pattern.index(shift_type) + shift_day - 1) % pattern_length
    days_passed = (reference_date.toordinal() - shift_index) % pattern_length
    return datetime.fromordinal(reference_date.toordinal() - days_passed)

# 식비 계산
def calculate_meal_allowance(start_date, end_date, shift_pattern, pattern_start_date, morning_holiday_count):
    meal_allowance = 0
    current_date = start_date
    pattern_length = len(shift_pattern)
    while current_date <= end_date:
        shift_type = shift_pattern[(current_date - pattern_start_date).days % pattern_length]
        if shift_type != "오전":
            meal_allowance += 8000
        current_date += timedelta(days=1)
    meal_allowance += morning_holiday_count * 8000
    return meal_allowance

# 식비 계산 후 메시지박스 출력
def calculate_and_show_allowance():
    reference_date = datetime.strptime(reference_date_entry.get(), '%Y-%m-%d')
    shift_type, shift_day = shift_info_entry.get().split()
    shift_day = int(shift_day)
    start_date = datetime.strptime(start_date_entry.get(), '%Y-%m-%d')
    end_date = datetime.strptime(end_date_entry.get(), '%Y-%m-%d')
    morning_holiday_count = int(morning_holiday_count_entry.get())

    pattern_start_date = calculate_pattern_start_date(shift_pattern, reference_date, shift_type, shift_day)

    meal_allowance = calculate_meal_allowance(start_date, end_date, shift_pattern, pattern_start_date, morning_holiday_count)
    messagebox.showinfo("식비 계산 결과", f"근무 기간 동안의 식비는 {meal_allowance}원입니다.")

# 근무 일정 출력
def show_shift_schedule():
    reference_date = datetime.strptime(reference_date_entry.get(), '%Y-%m-%d')
    shift_type, shift_day = shift_info_entry.get().split()
    shift_day = int(shift_day)
    start_date = datetime.strptime(start_date_entry.get(), '%Y-%m-%d')
    end_date = datetime.strptime(end_date_entry.get(), '%Y-%m-%d')

    pattern_start_date = calculate_pattern_start_date(shift_pattern, reference_date, shift_type, shift_day)

    schedule = ""
    current_date = start_date
    pattern_length = len(shift_pattern)
    while current_date <= end_date:
        shift_type = shift_pattern[(current_date - pattern_start_date).days % pattern_length]
        schedule += f"{current_date.strftime('%Y-%m-%d (%A)')}: {shift_type}\n"
        current_date += timedelta(days=1)

    messagebox.showinfo("근무 일정", schedule)

# 마지막 입력 값 저장
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

# 마지막 입력 값 불러오기
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

# GUI 설정
root = tk.Tk()

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

calculate_button = tk.Button(root, text="식비 계산하기", command=calculate_and_show_allowance)
calculate_button.pack()

show_schedule_button = tk.Button(root, text="근무 일정 표시하기", command=show_shift_schedule)
show_schedule_button.pack()

root.protocol("WM_DELETE_WINDOW", save_last_input)  # 프로그램이 종료될 때 마지막 입력 값을 저장
load_last_input()  # 프로그램이 시작될 때 마지막 입력 값을 불러옴

root.mainloop()
