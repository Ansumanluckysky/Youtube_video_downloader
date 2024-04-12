


from pytube import YouTube #This line imports the YouTube class from the pytube module. pytube is a Python library that provides an interface for downloading videos from YouTube.
import tkinter as tk  #This line imports the tkinter module, which is Python's standard GUI (Graphical User Interface) toolkit, as tk. tkinter allows you to create graphical user interfaces for your Python programs.
from tkinter import filedialog #filedialog provides a way to open file dialogs for selecting files or directories.

def download_video(url, save_path):
    try:
        yt = YouTube(url) #This line creates a new YouTube object by passing the url to the constructor. This object represents the YouTube video and provides methods for accessing information about the video and downloading it.
        streams = yt.streams.filter(progressive=True, file_extension="mp4") #This line filters the available streams (versions) of the video to only include those that are progressive (not adaptive) and have the file extension ".mp4". Streams are different versions of the video with varying resolutions and formats.
        highest_res_stream = streams.get_highest_resolution() #This line selects the stream with the highest resolution from the filtered list of streams. This is the stream that will be downloaded.
        highest_res_stream.download(output_path=save_path) #This line downloads the selected stream and saves it to the specified save_path directory.

        print("Video downloaded successfully!")
    except Exception as e:
        print(e)

def open_file_dialog():
    folder = filedialog.askdirectory() #This line opens a file dialog that allows the user to select a directory. The selected directory path is stored in the variable folder.
    if folder:
        print(f"Selected folder: {folder}")

    return folder



if __name__ == "__main__": #This line checks if the script is being run directly (not imported as a module). It's a common Python idiom to define code that should only be executed when the script is run directly inside this block.
    root = tk.Tk() #This line creates a new instance of the Tk class, which represents the main window of the application.
    root.withdraw() #This line hides the main window of the application. The main window is not needed in this program since we're only using file dialogs.

    video_url = input("Please enter a YouTube url: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Started download...")
        download_video(video_url, save_dir)
    else:
        print("Invalid save location.")

# url="https://youtu.be/lgUwYwBozow?list=PLdpzxOOAlwvIKMhk8WhzN1pYoJ1YU8Csa"
# save_path="E:/python/techwithtim projects/Youtube_video_downloader"
# download_video(url,save_path)