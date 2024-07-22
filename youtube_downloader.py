import yt_dlp
import os


# download youtube video
def downloader(videoid):
    '''
    yt_dlp. For details please visit: https://github.com/yt-dlp/yt-dlp
    Here, we define the format for video and audio. We download the best quality video and audio
    available on Youtube. The output format is mp4. The default folder to save downloaded video are
    ./download_youtube.
    '''
    ydl_opts = {
        'format': 'bestvideo+bestaudio',
        'merge_output_format': 'mp4',          # Merge into mp4 format
        'outtmpl': './download_youtube/%(id)s.%(ext)s',
        'ignore-errors': True
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f'https://www.youtube.com/watch?v={videoid}'])

    except Exception as error:
        print('Error: ', error)

downloader('PCicKydX5GE')