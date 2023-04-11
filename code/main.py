from youtube_to_mp3 import YoutubeConverter

def main():
    songs = []
    ask_for_input = True

    print("Enter songs you want to download...")
    while(ask_for_input):
        artist = str(input("Artist: "))
        title = str(input("Title: "))
        songs.append((artist, title))

        more_songs = str(input("Add more songs? (Y/N): "))
        if more_songs == "N":
            break
    
    converter = YoutubeConverter(songs)
    converter.crawl_and_download()
 
    destination_dir = str(input("Destination directory: "))
    converter.move_mp3_files(destination_dir)


if __name__ == "__main__":
    main()
    