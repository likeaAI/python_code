import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

meal_allowance = 10000
shift_pattern = ["오전"]*5 + ["휴무"] + ["오후"]*5 + ["휴무"]*2 + ["야간"]*5 + ["휴무"]*2

def calculate_pattern_start_date(shift_pattern, reference_date, shift_type, shift_day):
    pattern_length = len(shift_pattern)
    reference_index = shift_pattern.index(shift_type) + shift_day - 1
    pattern_start_date = reference_date - timedelta(days=reference_index % pattern_length)
    return pattern_start_date

def calculate_meal_allowance(start_date, end_date, shift_pattern, pattern_start_date, morning_holiday_count):
    total_allowance = 0
    current_date = start_date
    pattern_length = len(shift_pattern)
    while current_date <= end_date:
        shift_type = shift_pattern[(current_date - pattern_start_date).days % pattern_length]
        if shift_type != "휴무" or (shift_type == "오전" and morning_holiday_count > 0):
            total_allowance += meal_allowance
            if shift_type == "오전" and morning_holiday_count > 0:
                morning_holiday_count -= 1
        current_date += timedelta(days=1)
    return total_allowance

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

root = tk.Tk()

reference_date_label = tk.Label(root, text="근무 정보를 알고 있는 날짜 (YYYY-MM-DD):")
reference_date_label.pack()
reference_date_entry = tk.Entry(root)
reference_date_entry.pack()

shift_info_label = tk.Label(root, text="그 날의 근무 형태 및 진행 상태 (예: '오후 3'):")
shift_info_label.pack()
shift_info_entry = tk.Entry(root)
shift_info_entry.pack()

morning_holiday_count_label = tk.Label(root, text="오전 공휴일 수:")
morning_holiday_count_label.pack()
morning_holiday_count_entry = tk.Entry(root)
morning_holiday_count_entry.pack()

start_date_label = tk.Label(root, text="근무 시작일 (YYYY-MM-DD):")
start_date_label.pack()
start_date_entry = tk.Entry(root)
start_date_entry.pack()

end_date_label = tk.Label(root, text="근무 종료일 (YYYY-MM-DD):")
end_date_label.pack()
end_date_entry = tk.Entry(root)
end_date_entry.pack()

calculate_button = tk.Button(root, text="식비 계산하기", command=calculate_and_show_allowance)
calculate_button.pack()

root.mainloop()
