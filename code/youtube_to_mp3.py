import os
import shutil
import yt_dlp

from youtube_search import YoutubeSearch


class YoutubeConverter:
    def __init__(self, songs_to_convert):
        self.songs_to_convert = songs_to_convert
    

    def crawl_and_download(self):
        best_url = ""

        for song in self.songs_to_convert:
            artist = song[0]
            title = song[1]
            search_query = f"{artist} - {title}"

            results_list = YoutubeSearch(search_query, max_results=1).to_dict()
            best_url = "https://www.youtube.com{}".format(results_list[0]['url_suffix'])

            if best_url is None:
                print(f"No valid URLs found for {search_query}, skipping track.")
                continue
            print(f"Initiating download for {search_query}")

            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([best_url])
        
    
    def move_mp3_files(self, destination_dir):
        source_dir = '/home/joweid/Documents/Code/Python/youtube_to_mp3/code'

        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)
        
        for file_name in os.listdir(source_dir):
            if file_name.endswith('.mp3'):
                shutil.move(os.path.join(source_dir, file_name), destination_dir)
