import shutil
from pathlib import Path

directory = "/home/n3ura/Downloads/old/test"

categories = {
    "Images": [".jpg", ".png", ".jpeg", ".raw"],
    "Music": [".wav", ".aif", ".mp3", ".mid", ".m4r", ".nbs", ".iff", ".m3u", ".m4a", ".mid", ".mpa", ".wma", ".ogg", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
    "Iso": [".iso", ".img"],
    "Video": [".mpg", ".mov", ".wmv", ".rm", ".mp4", ".3g2", ".3gp", ".asf", ".avi", ".flv", ".m4v", ".srt", ".swf", ".vob", ".mkv", ".mpeg"],
    "Text": [".pdf", ".docx", ".eds", ".txt", ".epub", ".odt", ".rtf"],
    "Other": None
}


def create_directories():
    for folder in set(categories.keys()):
        Path(Path(directory).joinpath(folder)).mkdir(exist_ok=True)


def organizer(path):
    create_directories()
    for src_path in [x for x in Path(path).iterdir() if x.is_file()]:
        for dirname, extensions in categories.items():
            if extensions is None or src_path.name.endswith(tuple(extensions)):
                shutil.move(src_path, Path(directory).joinpath(dirname, src_path.name))
                break



if __name__ == '__main__':
    organizer(directory)
    print("Finished")