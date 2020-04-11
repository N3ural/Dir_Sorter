import shutil
import os
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


def get_subdirectories():
    sub_folders_names = [os.path.basename(x[0]) for x in os.walk(directory)]
    sub_folders_names.pop(0)
    return set(sub_folders_names)


def create_directories():
    folders_to_be_created = set(categories.keys()) - set(get_subdirectories())
    for folder in folders_to_be_created:
        os.mkdir(directory + "/" + folder)


def organizer(path):
    create_directories()
    for file in os.listdir(path):
        if os.path.isfile(path + "/" + file):
            src_path = path + "/" + file
            for dirname, extensions in categories.items():
                if extensions is None or file.endswith(tuple(extensions)):
                    dest_path = os.path.join(path, dirname, file)
                    shutil.move(src_path, dest_path)
                    break

if __name__ == '__main__':
    organizer(directory)
    print("finished")