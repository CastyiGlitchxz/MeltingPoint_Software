import os
import subprocess
import tkinter.filedialog
import tkinter
import customtkinter
from pytube import YouTube

SELECTED_PATH = ""

def startConversion():
    try:
        youtube_url = youtube_link_input.get()
        youtube_object = YouTube(youtube_url, on_progress_callback=on_progress)
        video_mp3 = youtube_object.streams.get_audio_only()
        download_status.configure(text="Download Completed!", text_color="green")
        video_mp3.download(output_path=SELECTED_PATH)
    except:
        download_status.configure(text="We've run into an error", text_color="red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    video_percentage_text.configure(text=per + '%')

    video_percentage_bar.set(float(percentage_of_completion) / 100)

def open_file_dialog():
    file_dialog = tkinter.filedialog.askdirectory(title="Select a folder to export your media")
    global SELECTED_PATH 
    SELECTED_PATH = file_dialog

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

# App Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("MeltingPoint Software")

insert_text = customtkinter.CTkLabel(app, text="Paste a YouTube link to continue")
insert_text.pack(padx=80, pady=80)

passed_url = tkinter.StringVar()
youtube_link_input = customtkinter.CTkEntry(app, width=350, height=40, textvariable=passed_url)
youtube_link_input.pack()

download_status = customtkinter.CTkLabel(app, text="")
download_status.pack()

video_percentage_text = customtkinter.CTkLabel(app, text="0%")
video_percentage_text.pack()

video_percentage_bar = customtkinter.CTkProgressBar(app, width=400)
video_percentage_bar.set(0)
video_percentage_bar.pack()

pack_button = customtkinter.CTkButton(app, text="Pack Files & Burn", command=startConversion)
pack_button.pack(padx="50", pady=50)

file_dialog_button = customtkinter.CTkButton(app, text="Select export dir", command=open_file_dialog)
file_dialog_button.pack()




# Run App
app.mainloop()