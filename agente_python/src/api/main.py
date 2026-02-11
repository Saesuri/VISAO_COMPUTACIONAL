from models import DetectionEvent
from event import EventSender

sender = EventSender("http://localhost:5000/api/eventos")

event = DetectionEvent("CAM01", "Red")
sender.send(event)
