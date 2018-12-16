import pafy
import os
import sys

if __name__ == '__main__':
    if not os.path.exists('Downloads'):
        os.mkdir("Downloads")
    print('Welcome to Youtube Downloader')
    url = input('Paste your URL here:')
    if url == 'close':
        sys.exit()
    else:
        ytb_url = pafy.new(url)
        audio_file = ytb_url.getbestaudio()
        print("Please wait... File will be ready soon...")
        os.chdir('Downloads')
        audio_file.download()
        print("Your song is ready :)")
        for file in os.listdir():
            title,ext = os.path.splitext(file)
            os.rename(file, title + '.mp3')