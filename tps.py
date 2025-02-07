import tkinter as tk
from tkinter import messagebox
from TikTokApi import TikTokApi

def stalk_tiktok_profile():
    username = entry.get()
    try:
        api = TikTokApi.get_instance()
        user = api.get_user(username)
        messagebox.showinfo("Success", f"Username: {user['user']['uniqueId']}\nFollowers: {user['stats']['followerCount']}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("TikTok Profile Stalking")
root.configure(bg='#000000')  # Hitam

frame = tk.Frame(root, bg='white', padx=20, pady=20)
frame.pack(pady=50)

label = tk.Label(frame, text="Masukkan Username TikTok", bg='white', fg='black', font=('Arial', 14))
label.pack(pady=10)

entry = tk.Entry(frame, width=40, font=('Arial', 12))
entry.pack(pady=10)

button = tk.Button(frame, text="Stalk Profile", bg='#000000', fg='white', font=('Arial', 12), command=stalk_tiktok_profile)
button.pack(pady=10)

root.mainloop()