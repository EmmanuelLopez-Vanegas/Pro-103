import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "ENTER THE PATH OF DOWNLOAD FOLDER (USE " / ") in VSC"
# to_dir = "ENTER THE PATH OF DESTINATION FOLDER(USE " / ") in VSC"

from_dir = "C:\\Users\\rocky\\Downloads"
to_dir = "C:\\Coding\\also class 102 - 103"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        name, extension = os.path.splittext(event.src_path)
        for key, value in dir_tree.items():
            if extension in value:
                file_name = os.path.basename(event.src_path)
                path1 = from_dir + "/" + file_name
                path2 = to_dir + "/" + key
                path3 = to_dir + "/" + key + "/" + file_name
                time.sleep(3)
                if os.path.exist(path2):
                    shutil.move(path1, path3)
                else:
                    os.mkdir(path2)
                    shutil.move(path1, path3)



# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stop")
    observer.stop()