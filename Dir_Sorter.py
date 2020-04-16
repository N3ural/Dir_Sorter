import shutil
from pathlib import Path
import time

directory = r"/home/n3ura/Downloads/old/test"

categories = {
    "Images": [".jpg", ".png", ".jpeg", ".raw", ".dng", ".cr2", ".nef", ".arw"],
    "Music": [".wav", ".aif", ".mp3", ".mid", ".m4r", ".nbs", ".iff", ".m3u", ".m4a", ".mid", ".mpa", ".wma", ".ogg", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
    "Iso": [".iso", ".img"],
    "Video": [".mpg", ".mov", ".wmv", ".rm", ".mp4", ".3g2", ".3gp", ".asf", ".avi", ".flv", ".m4v", ".srt", ".swf", ".vob", ".mkv", ".mpeg"],
    "Text": [".pdf", ".docx", ".eds", ".txt", ".epub", ".odt", ".rtf"],
    "Application": [".exe", ".app", ".vb", ".scr", ".msi", ".jar", ".ipa", ".apk", ".cgi", ".com", ".gadget", ".wsf", ".deb", ".rpm", ".pkg", ".pyc"],
    "Spreadsheet": [".xlsx", ".ods", ".numbers", ".xlr", ".xls"],
    "Torrent": [".torrent"],
    "Font":  [".otf", ".ttf", ".fnt", ".fon", ".otf"],
    "Other": None
}


def create_directories(path):
    for folder in set(categories.keys()):
        Path(Path(path).joinpath(folder)).mkdir(exist_ok=True)


def organizer(path):
    create_directories(path)
    for src_path in [x for x in Path(path).iterdir() if x.is_file()]:
        for dirname, extensions in categories.items():
            if extensions is None or src_path.name.endswith(tuple(extensions)):
                shutil.move(src_path, Path(directory).joinpath(dirname, src_path.name))
                break
    delete_empty_dir(path)

def delete_empty_dir(path):
    for elem in list(Path(path).iterdir()):
        if Path(elem).is_dir():
            delete_empty_dir(elem)
    if len(list(Path(path).iterdir())) == 0:
        Path(path).rmdir()

if __name__ == '__main__':
    start_time = time.time()
    organizer(directory)
    print("Finished")
    print("--- %s seconds ---" % (time.time() - start_time))

