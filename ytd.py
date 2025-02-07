import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

def download_youtube_video():
    url = entry.get()
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        messagebox.showinfo("Success", f"Downloaded: {yt.title}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("YouTube Downloader")
root.configure(bg='#FF0000')  # Merah

frame = tk.Frame(root, bg='white', padx=20, pady=20)
frame.pack(pady=50)

label = tk.Label(frame, text="Masukkan Link YouTube", bg='white', fg='black', font=('Arial', 14))
label.pack(pady=10)

entry = tk.Entry(frame, width=40, font=('Arial', 12))
entry.pack(pady=10)

button = tk.Button(frame, text="Download", bg='#FF0000', fg='white', font=('Arial', 12), command=download_youtube_video)
button.pack(pady=10)

root.mainloop()
