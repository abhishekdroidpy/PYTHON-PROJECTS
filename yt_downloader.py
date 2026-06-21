import pytube
import tkinter as tk
from tkinter import filedialog

def get_video():

    url = entry.get()

    save_path = filedialog.askdirectory()

    if not save_path:
        return

    try:

        status.config(text="Downloading...")
        root.update()

        yt = pytube.YouTube(url)

        streams = yt.streams.filter(
            progressive=True,
            file_extension="mp4"
        )

        high_res = streams.get_highest_resolution()

        high_res.download(output_path=save_path)

        status.config(text="VIDEO DOWNLOADED!")

    except Exception as e:

        status.config(text=str(e))


root = tk.Tk()

root.title("YOUTUBE DOWNLOADER")

entry = tk.Entry(root, width=50)
entry.pack(padx=20, pady=20)

button = tk.Button(
    root,
    text="DOWNLOAD",
    command=get_video
)

button.pack()

status = tk.Label(root, text="")
status.pack(pady=20)

root.mainloop()