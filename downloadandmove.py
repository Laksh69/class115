
import os 
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir="users/richakapoor/downloads"
to_dir="users/richakapoor/desktop/downloadedfiles"

dir_tree={
    "image_files":[".png",".jpg",".jpeg",".gif",".jfif",".svg"],
    "document_files":[".pdf",".doc",".docx",".txt",".csv"],
    "video_files":[".mpg",".mp2",".mpeg",".mpe",".mpv",".mp4",".m4p",".m4v",".avi",".mov"],
    "setup_files":[".exe",".bin",".cmd",".msi",".dmg"]
}

class FileMovementHandler(FileSystemEventHandler):
     def on_created(self,event):
      #   print(event)
         name,extension= os.path.splitext(event.src_path)
         time.sleep(1)
         for key,value in dir_tree.items():
             time.sleep(1)
             if extension in value:
                 fileName =os.path.basename(event.src_path)
                 print("downloaded " + fileName )
                 path1 = from_dir + "/" + fileName
                 path2 = to_dir + '/'+ key
                 path3 = to_dir + "/" + key + "/" +fileName
                 time.sleep(1)
                 if os.path.exists(path2):
                     time.sleep(1)
                     print("moving " + fileName + "...")
                     shutil.move(path1,path3)
                 else:
                      time.sleep(1)
                      os.makedirs(path2)
                      print("moving " + fileName + "...")
                      shutil.move(path1,path3)
event_handler=FileMovementHandler()
observer=Observer()
observer.schedule(event_handler,from_dir,recursive=True)
observer.start()

while True:
    time.sleep(2)
    print("running")