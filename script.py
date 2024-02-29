from pytube import YouTube
import ffmpeg  # Import the ffmpeg library
import os

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
if __name__ == "__main__":
    main("https://www.youtube.com/watch?v=C3lWwBslWqg")
    #clean_folder("./music")
