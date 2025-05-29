import yt_dlp

# Google Drive may NOT be fully supported — works for some public files only
video_urls = [
    'https://drive.google.com/file/d/1mWulNMu8JjsLK-Y5iR4AI_JF8BQkZuNo/view?t=7'
]

ydl_opts = {
    'outtmpl': r'D:\OneDrive - Advance IT Solution Enterprise\Code Rangers\Python Project\Download audio (MP3) from youtube\%(title)s.%(ext)s',
    'format': 'bestvideo+bestaudio/best',  # ✅ download full video + audio
    'merge_output_format': 'mp4',  # force output to mp4
    'noplaylist': True,
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(video_urls)
    print('Video downloaded successfully!')
except Exception as e:
    print(f"An error occurred: {e}")
