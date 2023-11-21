import tkinter as tk
from tkinter import filedialog
from pytube import YouTube

def download_video():
    video_url = url_entry.get()
    output_path = output_entry.get()
    selected_quality = quality_var.get()

    try:
        yt = YouTube(video_url, on_progress_callback=on_progress)
        video = yt.streams.filter(progressive=True, file_extension='mp4', resolution=selected_quality).first()
        if video:
            status_label.config(text=f"Downloading: {yt.title}...")
            video.download(output_path)
            status_label.config(text="Download complete!")
        else:
            status_label.config(text="No stream available for the selected quality.")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}")

def browse_output_path():
    folder_path = filedialog.askdirectory()
    output_entry.delete(0, tk.END)
    output_entry.insert(tk.END, folder_path)

def on_progress(stream, chunk, remaining):
    file_size = stream.filesize
    downloaded = file_size - remaining
    percent = (downloaded / file_size) * 100
    progress_label.config(text=f"Downloading... {percent:.1f}%")

root = tk.Tk()
root.title("YouTube Video Downloader")

url_label = tk.Label(root, text="Enter YouTube URL:")
url_label.pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

output_label = tk.Label(root, text="Select Output Path:")
output_label.pack()
output_entry = tk.Entry(root, width=50)
output_entry.pack()
browse_button = tk.Button(root, text="Browse", command=browse_output_path)
browse_button.pack()

quality_label = tk.Label(root, text="Select Quality:")
quality_label.pack()

quality_var = tk.StringVar()
quality_var.set("720p")
qualities = ["144p", "240p", "360p", "480p", "720p", "1080p"]

for quality in qualities:
    radio = tk.Radiobutton(root, text=quality, variable=quality_var, value=quality)
    radio.pack()

download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack()

progress_label = tk.Label(root, text="")
progress_label.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
