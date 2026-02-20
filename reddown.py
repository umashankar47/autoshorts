import yt_dlp


def download(url):
    print("Downloading Video")

    ydl_opts = {
    'format': 'bestvideo+bestaudio/best',  # Best video + audio
    'outtmpl': 'D:/DP/pyTon Env Testing/%(title)s.%(ext)s',  # Save to downloads folder
    'merge_output_format': 'mp4',  # Merge to mp4
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)

    return info['title']




if __name__ == '__main__':
    main()
