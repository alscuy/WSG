import tkinter as tk
from tkinter import messagebox
from instaloader import Instaloader, Profile

def stalk_instagram_story():
    username = entry.get()
    try:
        L = Instaloader()
        profile = Profile.from_username(L.context, username)
        stories = list(profile.get_stories())
        if stories:
            messagebox.showinfo("Success", f"Found {len(stories)} stories for {username}")
        else:
            messagebox.showinfo("Info", "No stories found")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("Instagram Story Stalking")
root.configure(bg='#FFC0CB')  # Pink

frame = tk.Frame(root, bg='white', padx=20, pady=20)
frame.pack(pady=50)

label = tk.Label(frame, text="Masukkan Username Instagram", bg='white', fg='black', font=('Arial', 14))
label.pack(pady=10)

entry = tk.Entry(frame, width=40, font=('Arial', 12))
entry.pack(pady=10)

button = tk.Button(frame, text="Stalk Story", bg='#FFC0CB', fg='white', font=('Arial', 12), command=stalk_instagram_story)
button.pack(pady=10)

root.mainloop()