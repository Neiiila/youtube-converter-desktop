import tkinter as tk
import tkinter.font as tkFont
from pytube import YouTube
import ffmpeg  # Import the ffmpeg library
import os


#************** converting process : 
# Step 1: Fetch the YouTube video
def fetch_video(url):
    try:
        yt = YouTube(url)
        return yt
    except Exception as e:
        print("Error fetching video:", e)
        return None

# Step 2: Download the video
def download_video(yt, output_path):
    try:
        stream = yt.streams.filter(only_audio=True).first()
        stream.download(output_path)
        return True
    except Exception as e:
        print("Error downloading video:", e)
        return False

# Step 3: Convert to MP3
def convert_to_mp3(video_path, output_path):
    try:
        ffmpeg.input(video_path).output(output_path).run()
        return True
    except Exception as e:
        print("Error converting to MP3:", e)
        return False

# Main function
def main(video_url):
    output_path = "./music"

    yt = fetch_video(video_url);
    print(yt.title)
    if yt:
        if download_video(yt, output_path):
            video_filename = yt.title + ".mp4"
            video_path = output_path + "/" + video_filename
            print(video_path)
            mp3_filename = yt.title + ".mp3"
            mp3_path = output_path + "/" + mp3_filename
            print(mp3_path)
            if convert_to_mp3(video_path, mp3_path):
                print("Video successfully converted to MP3:", mp3_path)
            else:
                print("Failed to convert video to MP3.")
        else:
            print("Failed to download video.")
    else:
        print("Invalid YouTube URL.")

def clean_folder(folder_path) : 
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        # Check if the file is a regular file and ends with ".mp4"
        if os.path.isfile(file_path) and file.endswith(".mp4"):
            try:
                # Delete the file
                os.remove(file_path)
            except OSError as e:
                print(f"Error deleting {file_path}: {e}")
    print("folder cleaned successfully")

## Interface 
def clear(event):
    list_urls.delete(0, tk.END)
    

    

def download(event):
    try : 
        for url in list_urls.get(0, tk.END):
            try:
        
                main(url)
            except Exception as e:
                print("Error downloading video:", e)
    except Exception as e:
        print("Error downloading video:", e)
    clean_folder("./music")    
def addLink(event):
    link = entry_url.get()
    list_urls.insert(tk.END, link)
    entry_url.delete(0, tk.END)
    
root = tk.Tk()
#setting title
root.title("youtube converter")
#setting window size
width=600
height=500
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

label_url=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
label_url["font"] = ft
label_url["fg"] = "#333333"
label_url["justify"] = "center"
label_url["text"] = "Youtube link :"
label_url["relief"] = "flat"
label_url.place(x=50,y=50,width=100,height=25)

entry_url=tk.Entry(root)
entry_url["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
entry_url["font"] = ft
entry_url["fg"] = "#333333"
entry_url["justify"] = "left"
entry_url["text"] = "Entry"
entry_url.place(x=160,y=50,width=405,height=30)
entry_url.bind("<Return>", addLink)

list_urls=tk.Listbox(root)
list_urls["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
list_urls["font"] = ft
list_urls["fg"] = "#333333"
list_urls["justify"] = "center"
list_urls.place(x=40,y=110,width=524,height=313)
list_urls["exportselection"] = "1"

clear_button=tk.Button(root)
clear_button["bg"] = "#f0f0f0"
ft = tkFont.Font(family='Times',size=10)
clear_button["font"] = ft
clear_button["fg"] = "#000000"
clear_button["justify"] = "center"
clear_button["text"] = "clear"
clear_button.place(x=220,y=440,width=70,height=25)
clear_button.bind('<Button-1>', clear) 

download_button=tk.Button(root)
download_button["bg"] = "#f0f0f0"
ft = tkFont.Font(family='Times',size=10)
download_button["font"] = ft
download_button["fg"] = "#000000"
download_button["justify"] = "center"
download_button["text"] = "download"
download_button.place(x=350,y=440,width=70,height=30)
download_button.bind('<Button-1>', download) 


root.mainloop()