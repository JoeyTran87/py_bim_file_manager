import sys
import time
import logging
import watchdog
from watchdog.observers import Observer
from watchdog.events import *

import os.path
import re
from watchdog.utils.patterns import match_any_paths


res = []

# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO,
#                         format='%(asctime)s - %(message)s',
#                         datefmt='%Y-%m-%d %H:%M:%S')
#     path = sys.argv[1] if len(sys.argv) > 1 else '.'
#     event_handler = LoggingEventHandler()
#     observer = Observer()
#     observer.schedule(event_handler, path, recursive=True)
#     observer.start()
#     try:
#         while True:
#             time.sleep(1)
#     finally:
#         observer.stop()
#         observer.join()

# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO,
#                         format='%(asctime)s - %(message)s',
#                         datefmt='%Y-%m-%d %H:%M:%S')
#     path = sys.argv[1] if len(sys.argv) > 1 else '.'
#     event_handler = LoggingEventHandler()
#     observer = Observer()
#     observer.schedule(event_handler, path, recursive=True)
#     observer.start()
#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         observer.stop()
#     observer.join()
class LoggingEventHandler2(FileSystemEventHandler):
    """Logs all the events captured."""
    res=[]
    def __init__(self, logger=None):
        super().__init__()
        self.logger = logger or logging.root

    def on_moved(self, event):
        super().on_moved(event)
        what = 'directory' if event.is_directory else 'file'
        self.logger.info("Moved %s: from %s to %s", what, event.src_path,
                         event.dest_path)
        self.res.append(f"Moved {what}: from {event.src_path} to {event.dest_path}")
    def on_created(self, event):
        super().on_created(event)
        what = 'directory' if event.is_directory else 'file'
        self.logger.info("Created %s: %s", what, event.src_path)
        self.res.append(f"Created {what}: {event.src_path}")

    def on_deleted(self, event):
        super().on_deleted(event)
        what = 'directory' if event.is_directory else 'file'
        self.logger.info("Deleted %s: %s", what, event.src_path)
        self.res.append(f"Deleted {what}: {event.src_path}")

    def on_modified(self, event):
        super().on_modified(event)
        what = 'directory' if event.is_directory else 'file'
        self.logger.info("Modified %s: %s", what, event.src_path)
        self.res.append(f"Modified {what}: {event.src_path}")

class HandlerJSON(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        # Set the patterns for PatternMatchingEventHandler
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.json'],
                                                             ignore_directories=True, case_sensitive=False)
  
    def on_created(self, event):
        print("Watchdog received created event - % s." % event.src_path)
        # Event is created, you can process it now
  
    def on_modified(self, event):
        print("Watchdog received modified event - % s." % event.src_path)
        # Event is modified, you can process it now
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = LoggingEventHandler2()#HandlerJSON()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(5)
            # print(len(event_handler.res))
    except KeyboardInterrupt:
        res = event_handler.res
        observer.stop()
    observer.join()


print(res)