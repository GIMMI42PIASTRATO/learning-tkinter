import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class FileModifiedHandler(FileSystemEventHandler):
    def __init__(self, filename):
        self.filename = filename

    def on_modified(self, event):
        print("Im here")
        if event.src_path.endswith(self.filename):
            print(f"Changes detected in {self.filename}. Reloading application...")
            os.execl(sys.executable, sys.executable, *sys.argv)


def watch_file_changes(filename):
    event_handler = FileModifiedHandler(filename)
    observer = Observer()
    observer.schedule(
        event_handler, path=os.path.dirname(os.path.abspath(__file__)), recursive=True
    )
    observer.start()
    try:
        print(f"Watching for changes in {filename}...")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping the observer...")
        observer.stop()
    observer.join()


if __name__ == "__main__":
    watch_file_changes("app.py")
