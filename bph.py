import os
import easygui as eg
import asyncio


async def audio_only(url,pth):
    print("ATTENTION: Audio download ONLY")
    # os.system(pth+"/BBDown "+url+" --audio-only")
    process = await asyncio.create_subprocess_exec(
        pth + "/BBDown", url, "--audio-only"
    )
    await process.wait()

async def video_download(url,pth):
    print("ATTENTION: Video Downloading")
    # os.system(pth+"/BBDown "+url)
    process = await asyncio.create_subprocess_exec(
        pth + "/BBDown", url
    )
    await process.wait()

async def main():
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
            # video_download(url,pth)
            asyncio.create_task(video_download(url,pth))
            await asyncio.sleep(0.1)
        if mode == "Audio Only":
            # audio_only(url,pth)
            asyncio.create_task(audio_only(url,pth))
            await asyncio.sleep(0.1)

if __name__ == "__main__":
    asyncio.run(main())