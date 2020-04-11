import shutil
from pathlib import Path

directory = "/home/n3ura/Downloads/old/test"

categories = {
    "Images": [".jpg", ".png", ".jpeg", ".raw"],
    "Music": [".wav", ".mp3", ".ogg", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
    "Iso": [".iso", ".img"],
    "Video": [".mp4", ".avi", ".mkv", ".mpeg"],
    "Text": [".pdf", ".docx", ".eds", ".txt"],
    "Other": None
}


def create_directories():
    for folder in set(categories.keys()):
        Path(directory + "/" + folder).mkdir(exist_ok=True)


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