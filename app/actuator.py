import json
import time
from collections import deque
from typing import Dict
from detector import ActuationEvent

class ActuationController:
    def __init__(self, num_nozzles=4, flow_rate_ml_per_ms=0.08):
        self.num_nozzles = num_nozzles
        self.flow_rate = flow_rate_ml_per_ms
        self.total_weeds_detected = 0
        self.total_intrarow_weeds = 0
        self.total_pulses_fired = 0
        self.total_herbicide_used_ml = 0.0
        self.broadcast_estimate_ml = 0.0
        self.event_log = deque(maxlen=100)
        self.fps_buffer = deque(maxlen=30)
        self.latency_buffer = deque(maxlen=30)
        self.start_time = time.time()
        self.recent_nozzles = set() # For UI mini-map
        self.last_nozzle_clear = time.time()

    def emit(self, event: ActuationEvent) -> Dict:
        herbicide_ml = event.pulse_ms * self.flow_rate
        self.total_pulses_fired += 1
        self.total_herbicide_used_ml += herbicide_ml
        self.broadcast_estimate_ml += 2.5 
        
        self.recent_nozzles.add(event.nozzle_id)

        payload = {
            "ts": time.strftime("%H:%M:%S", time.localtime(event.timestamp)),
            "track_id": event.track_id,
            "nozzle_id": event.nozzle_id,
            "pulse_ms": event.pulse_ms,
            "size_class": event.size_class,
            "occ_flag": "[OCC]" if event.occluded else "",
            "cmd": f"N{event.nozzle_id}:{event.pulse_ms}ms"
        }
        self.event_log.appendleft(payload)
        return payload

    def update_detection_stats(self, weeds, intrarow):
        self.total_weeds_detected += weeds
        self.total_intrarow_weeds += intrarow

    def update_perf(self, fps, latency_ms):
        self.fps_buffer.append(fps)
        self.latency_buffer.append(latency_ms)
        
        if time.time() - self.last_nozzle_clear > 0.4:
            self.recent_nozzles.clear()
            self.last_nozzle_clear = time.time()

    def get_metrics(self) -> Dict:
        avg_fps = sum(self.fps_buffer)/len(self.fps_buffer) if self.fps_buffer else 0
        avg_lat = sum(self.latency_buffer)/len(self.latency_buffer) if self.latency_buffer else 0
        saved_pct = 0.0
        if self.broadcast_estimate_ml > 0:
            saved_pct = max(0, (1 - self.total_herbicide_used_ml / self.broadcast_estimate_ml) * 100)
            saved_pct = min(92.0, saved_pct)
        
        return {
            "weeds_detected": self.total_weeds_detected,
            "pulses_fired": self.total_pulses_fired,
            "herbicide_saved_pct": round(saved_pct, 1),
            "avg_fps": round(avg_fps, 1),
            "avg_latency_ms": round(avg_lat, 1),
            "recent_nozzles": list(self.recent_nozzles)
        }
