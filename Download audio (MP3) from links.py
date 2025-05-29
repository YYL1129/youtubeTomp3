import yt_dlp

# Video URL for downloading
video_urls = [
    'https://drive.google.com/file/d/16iQ-aFYBNTEB8_u5PGI1Ap2VEn5fD-wQ/view'
]

# Options to download the best quality audio as MP3
ydl_opts = {
    'outtmpl': r'D:\OneDrive - Advance IT Solution Enterprise\Code Rangers\Python Project\Download audio (MP3) from youtube\%(title)s.%(ext)s',  # Save path and filename
    'format': 'bestaudio/best',  # Download the best available audio
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',  # Use FFmpeg to extract audio
        'preferredcodec': 'mp3',  # Convert audio to MP3 format
        'preferredquality': '192',  # Set audio quality to 256 kbps
    }],
    'noplaylist': True,  # Ensure only the single video is downloaded
}

# Download the audio
try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(video_urls)
    print('Audio downloaded successfully!')
except Exception as e:
    print(f"An error occurred: {e}")

