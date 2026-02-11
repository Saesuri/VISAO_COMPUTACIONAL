import requests
import threading
import queue
import time

class EventSender:

    def __init__(self, api_url):
        self.api_url = api_url
        self.event_queue = queue.Queue()
        self.worker = threading.Thread(target=self._process_queue, daemon=True)
        self.worker.start()

    def send(self, event):
        self.event_queue.put(event)

    def _process_queue(self):
        while True:
            event = self.event_queue.get()
            try:
                response = requests.post(
                    self.api_url,
                    json=event.to_dict(),
                    timeout=2
                )

                if response.status_code != 200:
                    print("Erro ao enviar:", response.status_code)

            except requests.RequestException as e:
                print("Falha na comunicação:", e)

            finally:
                self.event_queue.task_done()
