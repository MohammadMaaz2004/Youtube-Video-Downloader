from pytube import YouTube

def download_video(link, quality):
    try:
        print("Downloading....")
        YouTube(link).streams.filter(res=quality).first().download()
        print("Video Downloaded")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    link = input("Enter Youtube video link - ")
    print("\nVideo Quality")
    print("1.1080p")
    print("2.720p")
    print("3.480p")
    print("4.360p")
    quality = input("Please select the download Quality - ")
    quality_map = {"1": "1080p", "2": "720p", "3": "480p", "4": "360p"}
    download_video(link, quality_map.get(quality, "720p"))
