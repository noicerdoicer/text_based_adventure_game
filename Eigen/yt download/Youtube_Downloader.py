import os
import sys
from pathlib import Path
from pytube import YouTube

# link = input("Enter link here: ")

link = 'https://youtu.be/-ZGlaAxB7nI'

url = YouTube(link)

print("Select download format:")
print("1: Video file with audio (.mp4)")
print("2: Audio only (.mp3)")

media_type = input(">>")

if media_type == "1":
    video = url.streams.get_highest_resolution()

elif media_type == "2":
    video = url.streams.get_audio_only()
else:
    print("Invalid selection.")

print("downloading....")

# Disk Path for Downloaded Files for Text Adventure Game
path_to_download_folder = str(os.path.join(Path.home(), "Documents", "GitHub", "text_based_adventure_game", "Sounds"))
print(path_to_download_folder)




# Rename File according to specified File Name
custom_filename = input("File Name for downloaded content > ")

# MP4 Video + Audio
if media_type == "1":
    custom_filename = custom_filename+".mp4"

# MP3 Audio
elif media_type == "2":
    custom_filename = custom_filename + ".mp3"
else:
    print("Something went wrong")
    sys.exit()

# Download File with Custom
file = video.download(output_path=path_to_download_folder,filename=custom_filename)
os.system('cls')  # Clears the console
print(f'{file.title} has been Downloaded and was saved to the Disk! :)')
