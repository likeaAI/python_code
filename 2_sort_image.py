
""" 
# Specify the directory where you want to search for Python files
directory = "C:/Users/윤섭/Desktop/test"

# List of new names in the same order as the files
new_names = ["중조액상", "LNG 디지털" , "LNG 아날로그" , "디지털"]  # Add more names as needed

# List all files in the directory
files = [os.path.join(directory, f) for f in os.listdir(directory)]

# Sort the files by their modification date
files.sort(key=lambda x: os.path.getmtime(x), reverse=True)

print(files)

for i, file in enumerate(files):
    if i < len(new_names):
        _, file_extension = os.path.splitext(file)
        new_name = os.path.join(directory, new_names[i] + file_extension)
        try:
            print(f"Renaming {file} to {new_name}")
            os.rename(file, new_name)
        except Exception as e:
            print(f"Error renaming {file}: {e}")

# Print the renamed files
for new_name in os.listdir(directory):
    print(new_name)
"""


import os
import tkinter as tk
from tkinter import filedialog
import pickle

# Function to save new names to a binary file using pickle
def save_new_names(new_names):
    with open('new_names.pkl', 'wb') as file:
        pickle.dump(new_names, file)

def rename_files(directory, new_names):
    files = [os.path.join(directory, f) for f in os.listdir(directory)]
    files.sort(key=lambda x: os.path.getmtime(x), reverse=True)

    for i, file in enumerate(files):
        _, file_extension = os.path.splitext(file)
        new_name = os.path.join(directory, f"{new_names[i]}{file_extension}")
        try:
            os.rename(file, new_name)
        except Exception as e:
            print(f"Error renaming {file}: {e}")

def browse_directory():
    directory = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)
    directory_entry.insert(0, directory)

def start_rename():
    directory = directory_entry.get()
    new_names = new_names_entry.get().split(',')
    rename_files(directory, new_names)
    result_label.config(text="Files renamed successfully!")

# Create the main window
root = tk.Tk()
root.title("폴더사진 이름 변경")

# Create and configure widgets
directory_label = tk.Label(root, text="경로 지정:")
directory_label.pack()

directory_entry = tk.Entry(root, width=40)
directory_entry.pack()

browse_button = tk.Button(root, text="폴더선택", command=browse_directory)
browse_button.pack()

new_names_label = tk.Label(root, text="이름 변경 ('로 구분 ex)고양이,개,소 ):")
new_names_label.pack()

new_names_entry = tk.Entry(root, width=40)
new_names_entry.pack()

rename_button = tk.Button(root, text="파일이름 변경", command=start_rename)
rename_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Start the GUI main loop
root.mainloop()
