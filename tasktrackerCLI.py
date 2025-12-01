import json
import datetime

filename = "tasks.json"

def taskCreated(taskId, taskName,status, timestamp=None):
    if timestamp is None:
        timestamp = datetime.datetime.now().isoformat()
        event = {
            event: "taskCreated",
            "taskId": taskId,
            "taskName": taskName,
            "status": status,
            "timestamp": timestamp
        }
        print(json.dumps(event))