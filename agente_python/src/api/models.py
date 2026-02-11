from dataclasses import dataclass
from datetime import datetime

@dataclass
class DetectionEvent:
    camera_id: str
    color: str

    def to_dict(self):
        return {
            "cameraId": self.camera_id,
            "color": self.color,
            "timestamp": datetime.utcnow().isoformat()
        }
