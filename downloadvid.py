from pytube import YouTube

Base_youtube_url="https://www.youtube.com"

while True:
    url= input("Please enter the url of youtube video: ")

    if url.lower().startswith(Base_youtube_url):
      break


    print('Error: you need to enter a youtube video link!')

def on_download_progress(stream, chunk, bytes_remaining):
       byte_download = stream.filesize - bytes_remaining
       percentage = byte_download* 100/ stream.filesize

       print(f"Downloading...{int(percentage)}")
       

youtube_video = YouTube(url)

youtube_video.register_on_progress_callback(on_download_progress)
print()
print("Title: ", youtube_video.title)
print("Number of views: ", youtube_video.views)

stream = youtube_video.streams.get_highest_resolution()
print("Loading...")
stream.download()
print("Ok")