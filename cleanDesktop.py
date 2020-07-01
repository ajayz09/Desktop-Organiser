from pathlib import Path
from time import sleep
from watchdog.observers import Observer
from eventHandler import EventHandler

watch_path = Path.home() / 'Desktop'
organised_path = Path.home() / 'Desktop/Organiser'

event_handler = EventHandler(watch_path=watch_path, organised_path=organised_path)

observer = Observer()
observer.schedule(event_handler, f'{watch_path}', recursive=True)
observer.start()

try:
    while True:
        sleep(60)
except KeyboardInterrupt:
    observer.stop()
observer.join()