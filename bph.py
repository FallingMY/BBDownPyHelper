import os
import easygui as eg

#pip install easygui
#make sure you have installed easygui model

def audio_only(url,pth):
    print("ATTENTION: Audio download ONLY")
    os.system(pth+"/BBDown "+url+" --audio-only")

def video_download(url,pth):
    print("ATTENTION: Video Downloading")
    os.system(pth+"/BBDown "+url)




pth = os.getcwd()
pth = pth.replace("\\","/")

while True:
    url = eg.enterbox("Enter A Url of ONE video")
    if not url:
        break
    mode = eg.buttonbox("Choos A Download Mode","Mode Choose",["Cancel","Video","Audio Only"])
    if mode == "Cancel":
        break
    if mode == "Video":
        video_download(url,pth)
    if mode == "Audio Only":
        audio_only(url,pth)