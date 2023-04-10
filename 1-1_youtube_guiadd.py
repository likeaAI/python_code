import tkinter as tk
from tkinter import ttk, messagebox
from pytube import YouTube

def on_progress(stream, chunk, bytes_remaining):
    percentage = (1 - bytes_remaining / total_size) * 100
    progress_var.set(percentage)
    root.update()

def download_video():
    global total_size
    url = url_entry.get()
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")
        return

    resolution = resolution_var.get()
    if resolution == "720p":
        video = yt.streams.filter(progressive=True, file_extension="mp4").get_by_resolution("720p")
    elif resolution == "1080p":
        video = yt.streams.filter(progressive=False, file_extension="mp4").get_by_resolution("1080p")

    elif resolution == "2160p":
        video = yt.streams.filter(progressive="False", fps="60fps", vcodec="vp9", file_extension="mp4").first()
        if not video:
            video = yt.streams.filter(adaptive=True, file_extension="mp4").order_by("resolution").desc().first()

    if not video:
        messagebox.showerror("Error", "해당 해상도의 동영상을 찾을 수 없습니다.")
        return

    total_size = video.filesize

    try:
        video.download()
        messagebox.showinfo("Success", "다운로드가 완료되었습니다!")
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")

root = tk.Tk()
root.title("유튜브 동영상 다운로더 - chatgpt 사용")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

url_label = tk.Label(frame, text="동영상 URL:")
url_label.grid(row=0, column=0, sticky="w")
url_entry = tk.Entry(frame, width=40)
url_entry.grid(row=0, column=1)

resolution_label = tk.Label(frame, text="해상도 선택:")
resolution_label.grid(row=1, column=0, sticky="w")
resolution_var = tk.StringVar(value="720p")
resolution_720p = tk.Radiobutton(frame, text="720p", variable=resolution_var, value="720p")
resolution_720p.grid(row=1, column=1, sticky="w")
resolution_1080p = tk.Radiobutton(frame, text="1080p", variable=resolution_var, value="1080p")
resolution_1080p.grid(row=1, column=1, padx=(60, 0), sticky="w")
resolution_2160p = tk.Radiobutton(frame, text="2160p", variable=resolution_var, value="2160p")
resolution_2160p.grid(row=1, column=1, padx=(120, 0), sticky="w")

download_button = tk.Button(frame, text="다운로드", command=download_video)
download_button.grid(row=2, columnspan=2, pady=(10, 0))

progress_var = tk.DoubleVar(value=0)
progress_bar = ttk.Progressbar(frame, variable=progress_var, maximum=100)
progress_bar.grid(row=3, columnspan=2, pady=(10, 0), sticky="ew")

root.mainloop()
