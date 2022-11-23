from pytube import YouTube
import os

user_url = YouTube(str(input('enter your video url: \n>> ')))
video = user_url.streams.filter(res='360p').first()
print('where do you want to save your video')
destination = str(input('>> ')) or '. '    
file = video.download(output_path=destination)

base, ext =os.path.splitext(file)
new_file = base + '.mp4'
os.rename(file, new_file)

print(video.title + 'has been successfully downloaded' )